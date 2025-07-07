from flask import Flask, redirect, request
import requests
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get credentials from .env
CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")
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


@app.route("/authorised")
def authorised():
    ACCESS_CODE = request.args.get("code")
    # Send request to https://www.strava.com/oauth/token
    tokenReqURL = "https://www.strava.com/oauth/token"
    tokenReqResponse = requests.post(
        tokenReqURL,
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": ACCESS_CODE,
            "grant_type": "authorization_code",
        },
    )
    return f"Access Code: {ACCESS_CODE} \n Response JSON: {tokenReqResponse.json()}"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
