import json

def parse_suricata(log_path):
    alerts = []
    try:
        with open(log_path, 'r') as f:
            lines = f.readlines()
        for line in lines[-100:]:
            log = json.loads(line)
            if 'alert' in log:
                alerts.append({
                    'timestamp': log.get('timestamp'),
                    'src_ip': log.get('src_ip'),
                    'dest_ip': log.get('dest_ip'),
                    'alert': log['alert']['signature'],
                    'severity': log['alert']['severity']
                })
    except Exception as e:
        alerts.append({'error': str(e)})
    return alerts

