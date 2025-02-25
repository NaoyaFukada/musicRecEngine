import requests
import urllib.parse
from config import TokenManager

def get_artist_song_id(track_name, artist_name=None, market="US", limit = 1):

    # Instantiate the TokenManager
    token_manager = TokenManager()

    # Get the access token
    access_token = token_manager.get_access_token()

    # Print the token
    print("Access Token:", access_token)

    BASE_URL = "https://api.spotify.com/v1/search"

    # Constructing query parameters
    query = f"track:{track_name} artist:{artist_name}"
    if artist_name == None:
        query = f"track:{track_name}"
    encoded_query = urllib.parse.quote_plus(query)

    url = f"{BASE_URL}?q={encoded_query}&type=track&market={market}&limit={limit}"

    print("url", url)

    # Headers for authorization
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Parse JSON response
    data = response.json()

    if "tracks" in data and "items" in data["tracks"] and data["tracks"]["items"]:
        track = data["tracks"]["items"][0]
        track_id = track["id"]
        track_name = track["name"]
        track_url = track["external_urls"]['spotify']
        artist_id = track["artists"][0]["id"]
        artist_name = track["artists"][0]["name"]


        print(f"Track ID: {track_id}")
        print(f"Track Name: {track_id}")
        print(f"Track URL: {track_url}")
        print(f"Artist ID: {artist_id}")
        print(f"Artist Name: {artist_name}")
    else:
        print("No track found")

    return track_id, artist_id

print(get_artist_song_id("Best Friend", "Rex Orange County"))


