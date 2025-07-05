from flask import Flask, redirect, request
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get credentials from .env
CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
REDIRECT_URI = os.getenv("STRAVA_REDIRECT_URI")

# Create flask app
app = Flask(__name__)


@app.route("/")
def home():
    # This is where we generate the authorization URL
    auth_url = (
        f"https://www.strava.com/oauth/authorize?"
        f"client_id={CLIENT_ID}"
        f"&response_type=code"
        f"&redirect_uri={REDIRECT_URI}"
        f"&approval_prompt=auto"
        f"&scope=activity:read"
    )
    return f'<a href="{auth_url}">Connect to Strava</a>'
