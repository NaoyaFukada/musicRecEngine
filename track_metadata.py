import os
import json
from collections import defaultdict

class TrackMetaData:
    """
    A class to manage the track metadata for your application.
    
    This class is responsible for loading, saving, and retrieving track metadata
    from a JSON file. It uses a defaultdict to provide a default dictionary
    structure for missing keys.
    """

    def __init__(self, file_name="data/track_metadata.json"):
        # Define the file path for storing track metadata.
        self.file_name = file_name
        
        # Attempt to load existing track metadata from the file.
        # If the file doesn't exist, an empty file will be created.
        self.metadata_dict = self._load_file()

    def get(self, track_id):
        """
        Retrieves the metadata for a given track ID.
        
        :param track_id: The unique identifier of the track.
        :return: A dictionary of metadata for the track, or None if not found.
        """
        return self.metadata_dict.get(track_id, None)
    
    def set(self, tracks):
        """
        Sets metadata for multiple tracks.

        :param tracks: A list of dictionaries, where each dictionary contains track details with keys:
                   "track_id", "track_name", "track_url", "popularity", "artist_id", "artist_name".
        """
        for track in tracks:
            # Extract track details from the provided dictionary.
            track_id = track["track_id"]
            track_name = track["track_name"]
            track_url = track["track_url"]
            popularity = track["popularity"]
            artist_id = track["artist_id"]
            artist_name = track["artist_name"]

            # If this track is not already in the metadata dictionary,
            # add it with the provided information.
            if track_id not in self.metadata_dict:
                self.metadata_dict[track_id] = {
                    "track_name": track_name,
                    "track_url": track_url,
                    "popularity": popularity,
                    "artist_id": artist_id,
                    "artist_name": artist_name
                }
        self._save_file()

    def _save_file(self):
        """
        Saves the current track metadata dictionary to the JSON file.
        
        It ensures that the directory exists before saving.
        """
        # Ensure the directory for the file exists.
        os.makedirs(os.path.dirname(self.file_name), exist_ok=True)
        
        # Open the file in write mode and dump the metadata dictionary as JSON.
        with open(self.file_name, "w") as file:
            json.dump(self.metadata_dict, file, indent=4)

    def _load_file(self):
        """
        Loads track metadata from the JSON file.

        - If the file does not exist, it creates an empty JSON file and returns an empty metadata dictionary.
        - If the file exists, it attempts to load and return the metadata.
        - If the file contains invalid JSON, the program exits with an error message.
    
        :return: A defaultdict containing track metadata.
        """
        # Check if the metadata file exists.
        if not os.path.exists(self.file_name):
            print("⚠️ No existing track metadata file. Creating a new file.")
            os.makedirs(os.path.dirname(self.file_name), exist_ok=True)
            
            # Create an empty JSON file
            with open(self.file_name, "w") as file:
                json.dump({}, file, indent=4)
            return defaultdict(dict)
        
        try:
            # Open and read the JSON file.
            with open(self.file_name, "r") as file:
                # Reads JSON data from a file and converts it to Python Dictionary
                track_metadata = json.load(file)
                # Convert loaded dictionary into a defaultdict.
                return defaultdict(dict, track_metadata)
            print("✅ Track metadata successfully loaded from file.")
        except Exception as e:
            # If any error occurs (e.g., invalid JSON), exit the program.
            raise SystemExit(f"Exiting program due to some issues while loading the track metadata file: {e}")
        