from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def dashboard():

    threats = [
        {
            "ip": "185.220.101.1",
            "country": "Russia",
            "severity": "Critical",
            "type": "Botnet"
        },
        {
            "ip": "45.33.32.156",
            "country": "China",
            "severity": "High",
            "type": "Malware"
        },
        {
            "ip": "103.21.244.0",
            "country": "North Korea",
            "severity": "Medium",
            "type": "Phishing"
        },
        {
            "ip": "91.198.174.192",
            "country": "Iran",
            "severity": "Critical",
            "type": "Ransomware"
        }
    ]

    stats = {
        "total_attacks": random.randint(1000, 5000),
        "critical": random.randint(50, 150),
        "malware": random.randint(100, 300),
        "phishing": random.randint(70, 200)
    }

    return render_template('index.html', threats=threats, stats=stats)

if __name__ == '__main__':
    app.run(debug=True)