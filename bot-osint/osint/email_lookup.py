import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HIBP_API_KEY")
HEADERS = {
    "hibp-api-key": API_KEY,
    "user-agent": "osint-bot-telegram"
}

def lookup_email(email):
    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=true"
        res = requests.get(url, headers=HEADERS)

        if res.status_code == 404:
            return f"✅ Email *{email}* aman, tidak ditemukan dalam kebocoran publik."

        if res.status_code == 200:
            breaches = res.json()
            sites = [b['Name'] for b in breaches]
            site_list = "\n- " + "\n- ".join(sites)
            return f"""
⚠️ Email *{email}* ditemukan dalam *{len(breaches)}* kebocoran:
{site_list}
"""
        return f"⚠️ Error: Status code {res.status_code}"

    except Exception as e:
        return f"❌ Gagal cek email: {str(e)}"

