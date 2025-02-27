import json
from collections import defaultdict
import os
import itertools

class MusicGraph:
    def __init__(self):
        """
        Initializes the graph structure and supporting dictionaries.
        """
        self.music_graph = defaultdict(dict)  # Adjacency list (weighted graph)
        self.music_graph_file_name = "data/music_graph.json"
        self.user_favorite_songs = set()
        self.track_metadata = {}

    def add_a_track(self, track):
        """
        Add a new track to the graph if they are not already present and also add it to user_favorite_songs
        """
        track_id, track_name, track_url, popularity, artist_id, artist_name = track
        if track_id not in self.track_metadata:
            self.track_metadata[track_id] = {
                "track_name": track_name,
                "track_url": track_url,
                "popularity": popularity,
                "artist_id": artist_id,
                "artist_name": artist_name
            }
        self.user_favorite_songs.add(track_id)

    def add_tracks(self, tracks_list):
        """
        Adds new tracks to the graph if they are not already present.
        """
        tracks_id_list = []
        for track in tracks_list:
            track_id, track_name, track_url, popularity, artist_id, artist_name = track

            if track_id not in self.music_graph:
                self.track_metadata[track_id] = {
                    "track_name": track_name,
                    "track_url": track_url,
                    "popularity": popularity,
                    "artist_id": artist_id,
                    "artist_name": artist_name
                }

    def set_weight_by_spotify(self, tracks_list):
        for track1, track2 in itertools.combinations(tracks_list, 2):
            track1_id = track1["track_id"]
            tracl1_popularity = track1["popularity"]
            track2_id = track2["track_id"]
            tracl2_popularity = track2["popularity"]
            weights = round((tracl1_popularity + tracl2_popularity) / 20, 2)
            self.music_graph[track1_id][track2_id] = weights
            self.music_graph[track2_id][track1_id] = weights
        self.save_music_graph()

    def load_music_graph(self):
        if not os.path.exists(self.music_graph_file_name):
            print("⚠️ No existing music graph file found. Creating a new file.")

            os.makedirs(os.path.dirname(self.music_graph_file_name), exist_ok=True)
            
            # Create an empty JSON file
            with open(self.music_graph_file_name, "w") as file:
                json.dump({}, file, indent=4)

            return
        
        try:
            with open(self.music_graph_file_name, "r") as file:
                # Reads JSON data from a file and converts it to Python Dictionary
                music_graph_data = json.load(file)
                self.music_graph = defaultdict(dict, music_graph_data)
            print("✅ Graph successfully loaded from file.")
        except:
            raise SystemExit("Exiting program due to some issues while loading the music graph file.")
    
    def save_music_graph(self):
        """Saves the graph structure to a JSON file."""
        os.makedirs(os.path.dirname(self.music_graph_file_name), exist_ok=True)
        with open(self.music_graph_file_name, "w") as file:
            json.dump(self.music_graph, file, indent=4)

