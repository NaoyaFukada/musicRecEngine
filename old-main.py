from spotify_client import SpotifyClient
from music_graph import MusicGraph
from track_metadata import TrackMetaData

# Mock Data
# track_name = "We Are Never Ever Getting Back Together"
# artist_name = "Taylor Swift"
# market = "US"

# Instantiate imported classes
spotify_client = SpotifyClient()
music_graph= MusicGraph()
track_metadata = TrackMetaData()

# Main
def ask_user_favorite_track():
    track_name = input("What is your favorite track?").strip()
    artist_name = input("Do you know who sing this song?").strip()
    market = input("Which market is it? US or JP")
    searched_track_details = spotify_client.search_song(track_name, artist_name, market, limit=5)
    return searched_track_details

searched_track_details = None
popular_track_lists_by_artist = None

for track_details in tracks_details:
    if track_details["track_name"] == track_name and track_details["artist_name"] == artist_name:
        searched_track_details = track_details
        print("search_track", searched_track_details)
        track_metadata.set([searched_track_details])
        music_graph.add_by_user_interaction(searched_track_details, track_metadata)
        break

if searched_track_details:
   popular_track_lists_by_artist = spotify_client.get_popular_songs_by_artist(searched_track_details["artist_id"], market)
   if searched_track_details not in popular_track_lists_by_artist:
        popular_track_lists_by_artist.append(searched_track_details)
        track_metadata.set(popular_track_lists_by_artist)
        music_graph.add_by_spotify(popular_track_lists_by_artist)
        recommendations = music_graph.dfs_recommendation(track_details["track_id"])
        # Print results
        print("\n🎵 Top Recommended Songs:")
        for rank, (track_id, weight, depth) in enumerate(recommendations, start=1):
            print(f"\n🔹 Rank {rank}:")
            print(f"   🎧 Track ID: {track_id}")
            print(f"   🔗 Connection Strength: {weight}")
            print(f"   📏 Depth: {depth}")


# if popular_track_lists_by_artist:
#     user_selected_tracks_by_recommendation = popular_track_lists_by_artist[0]
#     music_graph.add_by_user_interaction(user_selected_tracks_by_recommendation, track_metadata)










