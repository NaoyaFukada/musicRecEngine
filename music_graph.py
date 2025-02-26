import uuid
import json
from collections import defaultdict
import os

class MusicGraph:
    def __init__(self):
        """
        Initializes the graph structure and supporting dictionaries.
        """
        self.graph = defaultdict(dict)  # Adjacency list (weighted graph)
        self.track_metadata = {} # Stores metadata (title, artist, URL)


    def load_graph(self, filename="data/music_graph.json"):
        if not os.path.exists(filename):
            print("⚠️ No existing graph file found. Creating a new file.")

            os.makedirs(os.path.dirname(filename), exist_ok=True)
            
            # Create an empty JSON file
            with open(filename, "w") as file:
                json.dump({}, file, indent=4)

            return
        
        try:
            with open(filename, "r") as file:
                # Reads JSON data from a file and converts it to Python Dictionary
                data = json.load(file)
                self.graph = defaultdict(dict, data)
            print("✅ Graph successfully loaded from file.")
        except:
            raise SystemExit("Exiting program due to some issues while loading the graph file.")
        
MusicGraph = MusicGraph()
MusicGraph.load_graph()

