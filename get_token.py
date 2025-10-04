import requests
import json

API_KEY = "API_KEY"  # from Firebase console
EMAIL = "test@gmail.com"
PASSWORD = "PASSWORD"

url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"

payload = {
    "email": EMAIL,
    "password": PASSWORD,
    "returnSecureToken": True
}

response = requests.post(url, json=payload)
data = response.json()

if "idToken" in data:
    print("Your Firebase ID Token:\n")
    print(data["idToken"])
else:
    print("Error:", data)
