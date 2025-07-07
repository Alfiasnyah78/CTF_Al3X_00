import requests

def lookup_ip(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}")
        data = res.json()

        if data['status'] != 'success':
            return "❌ IP tidak ditemukan atau salah."

        return f"""
📡 IP: {ip}
🌍 Negara: {data['country']} ({data['countryCode']})
🏙️ Kota: {data['city']}
🏢 ISP: {data['isp']}
🕓 Zona Waktu: {data['timezone']}
📍 Lokasi: {data['lat']}, {data['lon']}
"""
    except Exception as e:
        return f"⚠️ Error saat mengambil data IP: {str(e)}"

