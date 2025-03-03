import json
from collections import defaultdict
import os
import itertools
import math
import heapq

class MusicGraph:
    
    def __init__(self, file_name = "data/music_graph.json"):
        # File name to read and load music graph data
        self.file_name = file_name

        self.graph_dict = self._load_music_graph_from_file()

        # Set to store track IDs that are marked as favorites by the user within a session.
        self.fav_tracks_set = set()

    def add_by_spotify(self, tracks):
        """
        Adds multiple tracks to the graph based on Spotify data.

        :param tracks: A list of dictionaries, where each dictionary contains:
                       "track_id", "track_name", "track_url", "popularity",
                       "artist_id", and "artist_name".
        """

        # Iterate over all unique pairs of tracks.
        for track1, track2 in itertools.combinations(tracks, 2):

            track1_id = track1["track_id"]
            track1_popularity = track1["popularity"]
            track2_id = track2["track_id"]
            track2_popularity = track2["popularity"]
            
            # Calculate an initial weight
            weight = round((track1_popularity + track2_popularity) / 20, 2)
            
            # Initialize the edge weight if it does not already exist.
            if track2_id not in self.graph_dict[track1_id]:
                self.graph_dict[track1_id][track2_id] = weight
            if track1_id not in self.graph_dict[track2_id]:
                self.graph_dict[track2_id][track1_id] = weight
        
        self._save_music_graph_to_file()

    def add_by_user_interaction(self, new_fav_track, track_metadata_instance):
        """
        Add a track to the music graph based on user interaction

        :param new_fav_track: A dictionary containing details of the new favorite track with keys:
                              "track_id", "track_name", "track_url", "popularity",
                              "artist_id", and "artist_name".
        """

        new_fav_track_id = new_fav_track["track_id"]
        new_fav_popularity = new_fav_track["popularity"]

        # Convert the favorite tracks set to a list for iteration.
        fav_tracks_list = list(self.fav_tracks_set)

        for fav_track_id in fav_tracks_list:
            # Retrieve metadata for each favorite track.
            fav_track_metadata = track_metadata_instance.get(fav_track_id)
            print("track_meta_data", fav_track_metadata)

            # Compute the default weight based on the average popularity of the two tracks.
            default_weight = max(round((int(fav_track_metadata["popularity"]) + int(new_fav_popularity)) / 20, 2), 0.01)

            # If there's no existing connection, initialize it.
            if new_fav_track_id not in self.graph_dict[fav_track_id]:
                # Lower popularity yields a higher initial weight.
                weight = 5 / default_weight  
                init_weight = round(default_weight + weight, 2)
                self.graph_dict[fav_track_id][new_fav_track_id] = init_weight
                self.graph_dict[new_fav_track_id][fav_track_id] = init_weight
            else:
                # If the relationship already exists, update the weight dynamically.
                current_weight = self.graph_dict[fav_track_id][new_fav_track_id]
                # Use logarithmic scaling to calculate a smoother increment.
                weight_increment = round(5 / (math.log1p(current_weight) + 1), 2)  # log1p(x) = log(x + 1)
                self.graph_dict[fav_track_id][new_fav_track_id] += weight_increment
                self.graph_dict[new_fav_track_id][fav_track_id] += weight_increment

        self._save_music_graph_to_file()
        # Add the new favorite track ID to the favorites set.
        self.fav_tracks_set.add(new_fav_track_id)
            
    def dfs_recommendation(self, start_track_id, max_depth=3, top_k=10):
        if start_track_id not in self.graph_dict:
            print("⚠️ Track not found in the graph.")
            return []
    
        visited = set()
        max_heap = []

        def dfs(current_track_id, depth, min_weight):
            if depth > max_depth:
                return 
            
            visited.add(current_track_id)

            for neighbor_id, weight in self.graph_dict[current_track_id].items():
                if neighbor_id not in visited:
                    # Use the minimum weight encountered along this path
                    new_weight = min(min_weight, weight)

                    # **Pruning: Stop exploring if the weight is too weak**
                    if len(max_heap) == top_k and new_weight <= -max_heap[0][0]:
                        continue  # Skip this path (not strong enough)

                    # Push the track into the max heap (negative weight since heapq is a min-heap)
                    heapq.heappush(max_heap, (-new_weight, depth, neighbor_id))

                    # Keep heap size limited to `top_k` elements
                    if len(max_heap) > top_k:
                        heapq.heappop(max_heap)

                    # Recursive DFS call
                    dfs(neighbor_id, depth + 1, new_weight)

            # Remove from visited set for other paths
            visited.remove(current_track_id)

        # Start DFS with infinite initial weight
        dfs(start_track_id, depth=1, min_weight=float('inf'))

        # Convert max heap to sorted list (descending order by weight)
        return sorted(
            [(track_id, -weight, depth) for weight, depth, track_id in max_heap],
            key=lambda x: (-x[1], x[2])  # Sort by weight (desc), then depth (asc)
        )

    def _load_music_graph_from_file(self):

        if not os.path.exists(self.file_name):
            print("⚠️ No existing music graph file found. Creating a new file.")
            os.makedirs(os.path.dirname(self.file_name), exist_ok=True)
            # Create an empty JSON file
            with open(self.file_name, "w") as file:
                json.dump({}, file, indent=4)
            return defaultdict(dict)
        
        try:
            with open(self.file_name, "r") as file:
                # Read JSON data from the file.
                graph_data = json.load(file)
                # Initialize self.graph_dict as a defaultdict with the loaded data.
                return defaultdict(dict, graph_data)
            print("✅ Graph successfully loaded from file.")
        except Exception as e:
            raise SystemExit(f"Exiting program due to some issues while loading the music graph file: {e}")
    
    def _save_music_graph_to_file(self):

        os.makedirs(os.path.dirname(self.file_name), exist_ok=True)
        with open(self.file_name, "w") as file:
            json.dump(self.graph_dict, file, indent=4)

