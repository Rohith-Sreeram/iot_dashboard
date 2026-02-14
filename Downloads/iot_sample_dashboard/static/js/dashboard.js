const socket = io();

const tempValue = document.getElementById('temp-value');
const humValue = document.getElementById('hum-value');

// Chart Setup
const ctx = document.getElementById('tempChart').getContext('2d');
const MAX_DATA_POINTS = 20;

const tempChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Temperature (°C)',
            data: [],
            borderColor: '#00d2ff',
            backgroundColor: 'rgba(0, 210, 255, 0.1)',
            fill: true,
            tension: 0.4,
            pointRadius: 4,
            pointBackgroundColor: '#00d2ff',
            borderWidth: 3
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: false
            }
        },
        scales: {
            x: {
                grid: {
                    color: 'rgba(255, 255, 255, 0.05)'
                },
                ticks: {
                    color: '#94a3b8'
                }
            },
            y: {
                grid: {
                    color: 'rgba(255, 255, 255, 0.05)'
                },
                ticks: {
                    color: '#94a3b8'
                },
                suggestedMin: 15,
                suggestedMax: 40
            }
        },
        interaction: {
            intersect: false,
            mode: 'index'
        }
    }
});

socket.on('new_reading', (data) => {
    // Update numeric values
    tempValue.textContent = data.temperature.toFixed(1);
    humValue.textContent = data.humidity.toFixed(1);

    // Update Chart
    const now = data.timestamp;
    
    if (tempChart.data.labels.length >= MAX_DATA_POINTS) {
        tempChart.data.labels.shift();
        tempChart.data.datasets[0].data.shift();
    }
    
    tempChart.data.labels.push(now);
    tempChart.data.datasets[0].data.push(data.temperature);
    tempChart.data.update('none'); // Update without animation for performance if frequent
});

// For testing purposes, if you want to simulate data from the console:
// socket.emit('test_reading', {temperature: 25, humidity: 50, timestamp: '12:00:00'});
