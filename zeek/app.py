from flask import Flask, render_template, request
import os

app = Flask(__name__)

LOG_FILE = "/path/to/conn.log"  # ganti sesuai lokasi file Zeek kamu

def parse_zeek_log(file_path):
    if not os.path.exists(file_path):
        return []
    entries = []
    with open(file_path) as f:
        lines = f.readlines()

    header = []
    for line in lines:
        if line.startswith('#fields'):
            header = line.strip().split()[1:]  # ambil nama kolom
            continue
        if line.startswith('#') or line.strip() == '':
            continue
        parts = line.strip().split('\t')
        if len(parts) != len(header):
            continue
        entry = dict(zip(header, parts))
        entries.append(entry)
    return entries

@app.route('/', methods=['GET'])
def index():
    ip_filter = request.args.get('ip')
    entries = parse_zeek_log(LOG_FILE)
    if ip_filter:
        entries = [e for e in entries if ip_filter in (e.get('id.orig_h','') + e.get('id.resp_h',''))]
    return render_template('index.html', entries=entries, ip_filter=ip_filter)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=78, debug=True)

