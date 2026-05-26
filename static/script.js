const ctx1 = document.getElementById('threatChart');

new Chart(ctx1, {
    type: 'doughnut',
    data: {
        labels: ['Malware', 'Phishing', 'Botnet', 'Ransomware'],
        datasets: [{
            data: [35, 25, 20, 20],
            backgroundColor: [
                '#ef4444',
                '#facc15',
                '#3b82f6',
                '#22c55e'
            ]
        }]
    }
});

const ctx2 = document.getElementById('attackChart');

new Chart(ctx2, {
    type: 'line',
    data: {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        datasets: [{
            label: 'Attacks',
            data: [120, 190, 300, 250, 400, 350],
            borderColor: '#38bdf8',
            fill: false,
            tension: 0.4
        }]
    }
});