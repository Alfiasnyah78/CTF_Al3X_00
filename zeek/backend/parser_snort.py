def parse_snort(log_path):
    alerts = []
    try:
        with open(log_path, 'r') as f:
            lines = f.readlines()

        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith('[**]'):
                alert_msg = line.split(']')[2].strip()
                priority_line = lines[i+1].strip()
                time_ip_line = lines[i+2].strip()
                # Extract timestamp and IPs
                parts = time_ip_line.split()
                timestamp = parts[0] + " " + parts[1]
                src_ip = parts[2]
                dest_ip = parts[4]
                priority = priority_line.split(':')[1].strip().rstrip(']')
                alerts.append({
                    'timestamp': timestamp,
                    'src_ip': src_ip,
                    'dest_ip': dest_ip,
                    'alert': alert_msg,
                    'priority': priority
                })
                i += 3
            else:
                i += 1
    except Exception as e:
        alerts.append({'error': str(e)})
    return alerts

