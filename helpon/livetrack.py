from flask import Flask, request, jsonify, send_from_directory, render_template
import folium
import datetime
import os
import re
import phonenumbers
from phonenumbers import carrier, geocoder as ph_geocoder
from opencage.geocoder import OpenCageGeocode

app = Flask(__name__, static_folder='.')
TRACK_FILE = "bts_map.html"
IMSI_LOG = "/var/log/yatebts/ybts.log"
API_KEY = "de275befdb864cb09831cba0731ef382"

def mock_imsi_lookup(number):
    mock_imsi = {
        "+6281234567890": "510110123456789"
    }
    return mock_imsi.get(number)

# 2. Cek IMSI di log BTS
def is_target_connected(imsi):
    try:
        with open(IMSI_LOG, "r") as f:
            return any(imsi in line for line in f)
    except FileNotFoundError:
        return False

# 3. Ambil lokasi dari input nomor (geocoding area)
def geocode_number(number):
    try:
        parsed = phonenumbers.parse(number)
        location = ph_geocoder.description_for_number(parsed, "id")
        provider = carrier.name_for_number(parsed, "id")
        geo = OpenCageGeocode(API_KEY)
        result = geo.geocode(f"{location}, Indonesia")
        if result:
            return result[0]['geometry']['lat'], result[0]['geometry']['lng'], location, provider
    except Exception as e:
        print(f"[!] Geocode error: {e}")
    return None, None, None, None

# 4. Update peta lokasi terakhir
def update_map(lat, lng, label):
    myMap = folium.Map(location=[lat, lng], zoom_start=13, tiles='CartoDB positron')
    folium.Marker([lat, lng], tooltip="Target ditemukan", popup=label).add_to(myMap)
    folium.Circle([lat, lng], radius=200, color='red', fill=True, fill_opacity=0.3).add_to(myMap)
    myMap.save(TRACK_FILE)

# Endpoint utama
@app.route("/track-bts", methods=["POST"])
def track_bts():
    data = request.get_json()
    if not data or "number" not in data:
        return jsonify({"error": "Masukkan nomor telepon"}), 400

    number = data["number"]
    imsi = mock_imsi_lookup(number)
    if not imsi:
        return jsonify({"error": "IMSI tidak ditemukan untuk nomor ini"}), 404

    if not is_target_connected(imsi):
        return jsonify({"status": "Belum terhubung ke BTS"})

    lat, lng, location, provider = geocode_number(number)
    if not lat:
        return jsonify({"error": "Gagal geocode"}), 500

    update_map(lat, lng, f"{number} | {provider}")
    return jsonify({
        "status": "Target ditemukan di BTS",
        "imsi": imsi,
        "lat": lat,
        "lng": lng,
        "provider": provider
    })

# Dashboard real-time
@app.route("/dashboard")
def dashboard():
    return render_template("index.html")

# Serve map
@app.route("/map")
def serve_map():
    if os.path.exists(TRACK_FILE):
        return send_file(TRACK_FILE)
    return "Map belum dibuat. Jalankan tracking dulu.", 404



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

