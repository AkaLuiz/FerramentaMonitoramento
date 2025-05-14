function createChart(type, data, elementId = 'mainChart') {
    const ctx = document.getElementById(elementId).getContext('2d');
    
    // Destruir gráfico existente se houver
    if (window.currentChart) {
        window.currentChart.destroy();
    }

    window.currentChart = new Chart(ctx, {
        type: type === 'commits' ? 'line' : 'bar',
        data: {
            labels: data.labels,
            datasets: [{
                label: type === 'commits' ? 'Commits per Day' : 'Pull Requests per Day',
                data: data.values,
                borderColor: type === 'commits' ? '#2ea44f' : '#1f6feb',
                backgroundColor: type === 'commits' ? 'rgba(46, 164, 79, 0.2)' : 'rgba(31, 111, 235, 0.2)',
                borderWidth: 2,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1,
                        precision: 0
                    }
                }
            },
            plugins: {
                legend: {
                    display: true,
                    position: 'top'
                },
                tooltip: {
                    mode: 'index',
                    intersect: false
                }
            },
            interaction: {
                intersect: false,
                mode: 'nearest'
            },
            animation: {
                duration: 750,
                easing: 'easeInOutQuart'
            }
        }
    });
}

function initializeChartControls(commitData, pullData) {
    document.querySelectorAll('.chart-selector').forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            document.querySelectorAll('.chart-selector').forEach(btn => {
                btn.classList.remove('active');
            });
            
            // Add active class to clicked button
            this.classList.add('active');
            
            // Create appropriate chart
            const chartType = this.dataset.chart;
            const data = chartType === 'commits' ? commitData : pullData;
            createChart(chartType, data);
        });
    });
} 
