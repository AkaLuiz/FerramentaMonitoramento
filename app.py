from flask import Flask, render_template
import requests
from datetime import datetime, timedelta
from collections import defaultdict
import random
from config import GITHUB_TOKEN, REPOS

app = Flask(__name__)

HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}' if GITHUB_TOKEN else None,
    'Accept': 'application/vnd.github.v3+json'
}

def get_random_repo():
    return random.choice(REPOS)

def get_github_data(owner, repo):
    base_url = f"https://api.github.com/repos/{owner}/{repo}"
    since_date = (datetime.now() - timedelta(days=30)).isoformat()
    
    try:
        # Busca commits
        commits_response = requests.get(
            f"{base_url}/commits",
            headers=HEADERS,
            params={
                'since': since_date,
                'per_page': 100
            }
        )
        
        # Busca pull requests (incluindo fechados)
        pulls_response = requests.get(
            f"{base_url}/pulls",
            headers=HEADERS,
            params={
                'state': 'all',
                'sort': 'created',
                'direction': 'desc',
                'per_page': 100
            }
        )
        
        if commits_response.status_code == 200 and pulls_response.status_code == 200:
            commits = commits_response.json()
            pulls = pulls_response.json()
            
            # Debug info
            print(f"Fetched {len(commits)} commits and {len(pulls)} pull requests")
            print(f"Pull Requests data sample: {pulls[0] if pulls else 'No pulls'}")
            
            return commits, pulls
        else:
            print(f"API Response Status - Commits: {commits_response.status_code}, Pulls: {pulls_response.status_code}")
            return [], []
            
    except Exception as e:
        print(f"Error fetching data: {e}")
        return [], []

def process_date_data(items, date_key):
    data_by_date = defaultdict(int)
    thirty_days_ago = datetime.now() - timedelta(days=30)
    
    for item in items:
        try:
            if isinstance(date_key, str):
                date_str = item[date_key]
            else:
                date_str = date_key(item)
                
            date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
            
            # Apenas processa dados dos últimos 30 dias
            if date >= thirty_days_ago:
                date_formatted = date.strftime('%Y-%m-%d')
                data_by_date[date_formatted] += 1
                
        except (KeyError, TypeError) as e:
            print(f"Error processing date: {e}")
            continue
    
    # Preenche datas faltantes com zero
    all_dates = {}
    current_date = thirty_days_ago
    while current_date <= datetime.now():
        date_str = current_date.strftime('%Y-%m-%d')
        all_dates[date_str] = data_by_date.get(date_str, 0)
        current_date += timedelta(days=1)
    
    return dict(sorted(all_dates.items()))

@app.route('/')
def index():
    repo_info = get_random_repo()
    owner = repo_info['owner']
    repo = repo_info['repo']
    
    commits, pulls = get_github_data(owner, repo)
    
    commit_data = process_date_data(commits, lambda x: x['commit']['author']['date'])
    pull_data = process_date_data(pulls, 'created_at')
    
    return render_template('index.html',
                         commit_data=commit_data,
                         pull_data=pull_data,
                         repo_name=f"{owner}/{repo}",
                         repo_url=f"https://github.com/{owner}/{repo}")

@app.route('/repository')
def repository():
    repo_info = {
        "owner": "facebook",
        "repo": "react"
    }  # Usando um repositório fixo para teste
    
    commits, _ = get_github_data(repo_info['owner'], repo_info['repo'])
    
    # Adiciona URLs dos commits se não existirem
    for commit in commits:
        if 'html_url' not in commit:
            commit['html_url'] = f"https://github.com/{repo_info['owner']}/{repo_info['repo']}/commit/{commit['sha']}"
    
    return render_template('repository.html',
                         commits=commits[:10],  # Mostra os 10 commits mais recentes
                         repo_name=f"{repo_info['owner']}/{repo_info['repo']}",
                         repo_url=f"https://github.com/{repo_info['owner']}/{repo_info['repo']}")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
