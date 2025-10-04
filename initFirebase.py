from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer
import firebase_admin
from firebase_admin import credentials, auth
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Firebase Admin
cred_path = os.getenv("FIREBASE_CREDENTIALS", "Firebase_Credentials_File.json")
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

app = FastAPI()
security = HTTPBearer()

@app.get("/")
def root():
    return {"message": "Firebase Auth Running!"}

@app.get("/protected")
def protected_route(token: str = Depends(security)):
    try:
        decoded_token = auth.verify_id_token(token.credentials)
        user_id = decoded_token["uid"]
        email = decoded_token.get("email", "unknown")
        return {"message": f"Welcome, {email}! Your UID is {user_id}."}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
