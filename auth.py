import os
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from dotenv import load_dotenv

load_dotenv() 

def getToken():

    scopes = [
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/firebase.database"
    ]

    service_account_info = {
        "type": "service_account",
        "project_id": "thumbsapp-748bd",
        "private_key_id": os.getenv('PRIVATE_KEY_ID'),
        "private_key": os.getenv("PRIVATE_KEY"),
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-lirwh%40thumbsapp-748bd.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }   

    credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes=scopes)
    credentials.refresh(Request())

    return credentials.token