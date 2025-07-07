import requests

BASE_URL = "http://localhost:88"

def test_failed_logins():
    for i in range(5):
        r = requests.post(BASE_URL + "/", data={
            "username": "admin",
            "password": "wrong",
            "captcha_answer": "8",  # benar
            "captcha_expected": "8"
        })
        assert "Login failed" in r.text

def test_fail_captcha():
    r = requests.post(BASE_URL + "/", data={
        "username": "admin",
        "password": "whatever",
        "captcha_answer": "0",  # salah
        "captcha_expected": "10"
    })
    assert "Failed CAPTCHA" in r.text

