from spotify_client import SpotifyClient
from music_graph import MusicGraph

track_name = "We Are Never Ever Getting Back Together"
artist_name = "Taylor Swift"
market = "US"

# Instantiate Spotify client
spotify_client = SpotifyClient()
music_graph= MusicGraph()

# Search for a song (Example)
search_song_results = spotify_client.search_song(track_name, artist_name, market, limit=5)

searched_track = None
popular_track_lists_by_artist = None

for result in search_song_results:
    if result["track_name"] == track_name and result["artist_name"] == artist_name:
        searched_track = result
        print("search_track", searched_track)
        music_graph.add_a_track(searched_track)
        break

if searched_track:
   popular_track_lists_by_artist = spotify_client.get_popular_songs_by_artist(searched_track["artist_id"], market)
   if searched_track not in popular_track_lists_by_artist:
       popular_track_lists_by_artist.append(searched_track)
       music_graph.add_tracks(popular_track_lists_by_artist)
       music_graph.set_weight_by_spotify(popular_track_lists_by_artist)







