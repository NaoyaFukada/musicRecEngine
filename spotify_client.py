import requests
import urllib.parse
from config import TokenManager

class SpotifyClient:
    def __init__(self):
        """Initialize SpotifyClient and set up TokenManager."""
        self.token_manager = TokenManager()
    
    def search_song(self, track_name, artist_name=None, market="US", limit=5):
        """Search for songs on Spotify and return track details."""

        # Get the access token
        access_token = self.token_manager.get_access_token()

        BASE_URL = "https://api.spotify.com/v1/search"

        # Construct query parameters
        query = f"track:{track_name}"
        if artist_name:
            query += f" artist:{artist_name}"

        # Encode query for URL
        encoded_query = urllib.parse.quote_plus(query)
        url = f"{BASE_URL}?q={encoded_query}&type=track&market={market}&limit={limit}"

        # Debugging: Print request URL
        print(f"🔍 Searching for: {track_name} by {artist_name or 'Any'}")
        print(f"📡 Request URL: {url}")

        # Headers for authorization
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        # Make the GET request
        response = requests.get(url, headers=headers)

        # Handle request errors
        if response.status_code != 200:
            print(f"❌ Error: Failed to fetch songs ({response.status_code})")
            return []

        # Parse JSON response
        data = response.json()

        if "tracks" in data and "items" in data["tracks"] and data["tracks"]["items"]:
            results = [
                {
                    "track_id": track["id"],
                    "track_name": track["name"],
                    "track_url": track["external_urls"]['spotify'],
                    "artist_id": track["artists"][0]["id"],
                    "artist_name": track["artists"][0]["name"]
                }
                for track in data["tracks"]["items"]
            ]

            # Print results
            print("\n🎵 Search Results:")
            for idx, song in enumerate(results, start=1):
                print(f"\nResult {idx}:")
                print(f"Track ID: {song['track_id']}")
                print(f"Track Name: {song['track_name']}")
                print(f"Track URL: {song['track_url']}")
                print(f"Artist ID: {song['artist_id']}")
                print(f"Artist Name: {song['artist_name']}")

            return results  # Return all track details as a list
        
        else:
            print("⚠️ No track found.")
            return []
    
    def get_popular_songs_by_artist(self, artist_id, market="US"):
        """Get the most popular songs of an artist."""

        # Get the access token
        access_token = self.token_manager.get_access_token()

        url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market={market}"

        # Debugging: Print request URL
        print(f"🎤 Fetching top tracks for Artist ID: {artist_id}")
        print(f"📡 Request URL: {url}")

        # Headers for authorization
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        # Make the GET request
        response = requests.get(url, headers=headers)

        # Handle request errors
        if response.status_code != 200:
            print(f"❌ Error: Failed to fetch top tracks ({response.status_code})")
            return []

        # Parse JSON response
        data = response.json()

        # Ensure tracks exist before processing
        if "tracks" in data and data["tracks"]:
            results = [
                {
                    "track_id": track["id"],
                    "track_name": track["name"],
                    "track_url": track["external_urls"]['spotify'],
                    "popularity": track["popularity"]
                }
                for track in data["tracks"]
            ]

            # Print results
            print("\n🔥 Top Tracks:")
            for idx, song in enumerate(results, start=1):
                print(f"\nResult {idx}:")
                print(f"Track ID: {song['track_id']}")
                print(f"Track Name: {song['track_name']}")
                print(f"Track URL: {song['track_url']}")
                print(f"Popularity: {song['popularity']}")

            return results
        
        else:
            print("⚠️ No top tracks found.")
            return []

# Instantiate Spotify client
spotify_client = SpotifyClient()

# Search for a song (Example)
results = spotify_client.search_song("We are never ever getting back together", None, "JP", limit=3)

# Get top tracks for an artist (Example)
if results:
    artist_id = results[0]["artist_id"]
    top_songs = spotify_client.get_popular_songs_by_artist(artist_id, "JP")
