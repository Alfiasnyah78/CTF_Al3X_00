# backend/app.py
from flask import Flask, jsonify, request
from parser_suricata import parse_suricata
from parser_snort import parse_snort

app = Flask(__name__)

@app.route('/api/alerts/suricata')
def alerts_suricata():
    alerts = parse_suricata('/var/log/suricata/eve.json')
    return jsonify(alerts)

@app.route('/api/alerts/snort')
def alerts_snort():
    alerts = parse_snort('/var/log/snort/alert')
    return jsonify(alerts)

@app.route('/api/alerts')
def alerts_all():
    suricata = parse_suricata('/var/log/suricata/eve.json')
    snort = parse_snort('/var/log/snort/alert')
    return jsonify({
        'suricata': suricata,
        'snort': snort
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=78, debug=True)

