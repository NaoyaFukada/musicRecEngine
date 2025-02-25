import requests
import base64
import os
from dotenv import load_dotenv
import time

# Load environment variables from a .env file (recommended for security)
load_dotenv()

class TokenManager:
    """Manages the retrieval and storage of Spotify API access tokens."""
    
    def __init__(self):
        # Load credentials from environment variables
        self.__client_id = os.getenv("CLIENT_ID")
        self.__client_secret = os.getenv("CLIENT_SECRET")

        # Validate that the credentials are set
        if not self.__client_id or not self.__client_secret:
            raise ValueError("CLIENT_ID or CLIENT_SECRET is missing. Check your .env file.")

        self.access_token = None
        self.token_expiration = 0

    def get_access_token(self):
        """
        Fetches a fresh access token from the Spotify API using client credentials.
        If an access token is already available and valid, it is reused.
        """
        
        # Return cached token if it's still valid
        if self.access_token and time.time() < self.token_expiration:
            return self.access_token

        # Spotify API token endpoint
        url = "https://accounts.spotify.com/api/token"

        # Prepare Base64-encoded client credentials for authorization
        auth_str = f"{self.__client_id}:{self.__client_secret}"
        encoded_auth = base64.b64encode(auth_str.encode()).decode()

        # Request headers and data payload
        headers = {
            "Authorization": f"Basic {encoded_auth}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"grant_type": "client_credentials"}

        # Make a POST request to get a new token
        response = requests.post(url, headers=headers, data=data)
        response_data = response.json()

        # Process response and extract access token
        if "access_token" in response_data:
            self.access_token = response_data["access_token"]
            self.token_expiration = time.time() + response_data["expires_in"] - 5  # Subtract 5s buffer for safety
            return self.access_token
        else:
            raise Exception(f"Failed to get access token: {response_data}")
