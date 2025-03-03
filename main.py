from spotify_client import SpotifyClient
from music_graph import MusicGraph
from track_metadata import TrackMetaData

# Instantiate imported classes
spotify_client = SpotifyClient()
music_graph = MusicGraph()
track_metadata = TrackMetaData()

def ask_user_about_favorite_track():
    """
    Prompts the user for track name, artist name, and market (all optional, but at least one must be provided).
    Calls Spotify API to search for matches and lets the user select the correct track if multiple results exist.
    Returns the selected track details and its market.
    """
    
    while True:
        # Ask user for track and artist
        track_name = input("🎵 What is your favorite track? (Press Enter to skip) ").strip()
        artist_name = input("🎤 Do you know who sings your favorite song? (Press Enter to skip) ").strip()
        market = input("🌍 Which market is it? (US, JP, etc., or press Enter for default) ").strip()
        if not market:
            market = "US"

        # Ensure at least one of track name or artist name is provided
        if not track_name and not artist_name:
            print("⚠️ Please provide at least a track name or artist name.")
            continue

        # Search for matching songs using Spotify API
        searched_potential_tracks = spotify_client.search_song(track_name, artist_name, market, limit=5)
        searched_matched_tracks = []

        # Find matched result from searched potential tracks
        for searched_potential_track in searched_potential_tracks:
            # You can refine logic for "matching" below as needed:
            if (
                (track_name and searched_potential_track["track_name"].lower() == track_name.lower()) or 
                (artist_name and searched_potential_track["artist_name"].lower() == artist_name.lower())
            ):
                searched_matched_tracks.append(searched_potential_track)

        # If no "perfect" matches found, fall back to letting user pick from the raw search results
        if len(searched_matched_tracks) == 0 and len(searched_potential_tracks) > 0:
            print("No exact matches, but here are the top search results.")
            searched_matched_tracks = searched_potential_tracks

        if len(searched_matched_tracks) == 0:
            print("❌ No matching songs found. Please try again.\n")
            continue

        # If only 1 match found, confirm with user
        if len(searched_matched_tracks) == 1:
            track_found = searched_matched_tracks[0]
            confirmation = input(
                f"✅ Is this your song? {track_found['track_name']} by {track_found['artist_name']} (yes/no) "
            ).strip().lower()
            while confirmation not in ("yes", "no"):
                print("Your input is invalid. Try again.")
                confirmation = input(
                    f"✅ Is this your song? {track_found['track_name']} by {track_found['artist_name']} (yes/no) "
                ).strip().lower()

            if confirmation == "yes":
                return track_found, market
            else:
                print("🔁 Let's try again.\n")
                continue

        # If multiple results are found, let the user choose
        print("\n🔍 Multiple matches found. Please select the correct one:")
        for idx, track in enumerate(searched_matched_tracks, start=1):
            print(f"{idx}. {track['track_name']} by {track['artist_name']}")

        while True:
            try:
                selection = int(input("\nEnter the number of the correct song (or 0 to search again): "))
                if selection == 0:
                    break  # Restart search
                if 1 <= selection <= len(searched_matched_tracks):
                    return searched_matched_tracks[selection - 1], market
                else:
                    print("⚠️ Invalid choice. Please enter a valid number.")
            except ValueError:
                print("⚠️ Invalid input. Please enter a number.")


def pick_recommendations_loop(chosen_track_id):
    """
    Given a track_id, repeatedly get recommendations from the graph,
    let the user select favorites among the recommended tracks, and
    add them via user_interaction. Then let the user continue 
    recommending based on the *newly* selected track(s) or break.
    """
    while True:
        # 1) Get recommended track IDs from the graph
        # Format: [(track_id, weight, depth), (track_id, weight, depth), ...]
        recommendations = music_graph.dfs_recommendation(chosen_track_id)

        if not recommendations:
            print("No recommendations found for this track.")
            break

        # 2) Convert those track_ids into actual metadata
        recommended_tracks_with_metadata = []
        for (rec_track_id, weight, depth) in recommendations:
            data = track_metadata.get(rec_track_id)
            if data:
                recommended_tracks_with_metadata.append({
                    "rank": len(recommended_tracks_with_metadata) + 1,
                    "track_id": rec_track_id,
                    "track_name": data["track_name"],
                    "track_url": data["track_url"],
                    "popularity": data["popularity"],
                    "artist_id": data["artist_id"],
                    "artist_name": data["artist_name"],
                    "weight": weight,
                    "depth": depth
                })

        print("\n🎵 Top Recommended Songs:")
        for item in recommended_tracks_with_metadata:
            print(
                f"{item['rank']}. {item['track_name']} by {item['artist_name']} "
                f"(Weight={item['weight']}, Depth={item['depth']})"
            )

        if not recommended_tracks_with_metadata:
            print("⚠️ No metadata for recommended track IDs. Nothing to pick from.")
            break

        # 3) Prompt user to pick multiple from recommended tracks
        user_input = input(
            "\nEnter the number(s) of the track(s) you like (comma-separated), or press Enter to skip: "
        ).strip()

        new_chosen_track_id = chosen_track_id  # default if user doesn't pick anything

        if user_input:
            # Parse user selection
            try:
                selections = [int(x.strip()) for x in user_input.split(",")]
            except ValueError:
                print("⚠️ Invalid input. Skipping selection.")
                selections = []

            # For each selected track, add to the music graph via user_interaction
            for sel in selections:
                if 1 <= sel <= len(recommended_tracks_with_metadata):
                    selected_track = recommended_tracks_with_metadata[sel - 1]
                    track_dict = {
                        "track_id": selected_track["track_id"],
                        "track_name": selected_track["track_name"],
                        "track_url": selected_track["track_url"],
                        "popularity": selected_track["popularity"],
                        "artist_id": selected_track["artist_id"],
                        "artist_name": selected_track["artist_name"],
                    }
                    music_graph.add_by_user_interaction(track_dict, track_metadata)
                    print(f"✅ Added '{track_dict['track_name']}' ({track_dict['track_id']}) to your favorites.")
                else:
                    print(f"⚠️ {sel} is out of range. Skipping.")

            # If the user selected at least one track, let's do new recommendations
            # based on the **last** item in the selections:
            if selections:
                last_sel_index = selections[-1] - 1
                new_chosen_track_id = recommended_tracks_with_metadata[last_sel_index]["track_id"]

        # 4) Ask user how they want to proceed
        user_choice = input(
            "\nWould you like to:\n"
            "  [1] Get more recommendations (based on your *latest* selection)\n"
            "  [2] Search for a NEW favorite track\n"
            "  [3] Quit\n"
            "Enter your choice (1/2/3): "
        ).strip()

        if user_choice == "1":
            # Replace chosen_track_id with the newly selected track ID
            chosen_track_id = new_chosen_track_id
            # Loop continues from the top, offering more recs for new track
            continue
        elif user_choice == "2":
            # Break to let main() ask for a brand-new track
            break
        else:
            # user_choice == "3" or anything else => quit entirely
            print("👋 Quitting. Thank you!")
            exit(0)


def main():
    print("Welcome to the Interactive Music Recommender!")
    while True:
        # 1) Ask user for a track
        searched_track_detail, market = ask_user_about_favorite_track()
        if not searched_track_detail:
            continue

        # 2) Display user selection
        print(
            f"\n🎶 You selected: {searched_track_detail['track_name']} "
            f"by {searched_track_detail['artist_name']}\n"
        )
        
        # 3) Add the chosen track to metadata & music graph
        track_metadata.set([searched_track_detail])
        music_graph.add_by_user_interaction(searched_track_detail, track_metadata)

        # 4) Get popular songs by the same artist, and add them to metadata/graph
        popular_tracks_list_by_artist = spotify_client.get_popular_songs_by_artist(
            searched_track_detail["artist_id"], market
        )
        # Ensure user’s chosen track is included
        if searched_track_detail not in popular_tracks_list_by_artist:
            popular_tracks_list_by_artist.append(searched_track_detail)
        track_metadata.set(popular_tracks_list_by_artist)
        music_graph.add_by_spotify(popular_tracks_list_by_artist)

        # 5) Let the user pick from recommended tracks in a loop 
        #    (They can chain from selection to selection)
        pick_recommendations_loop(searched_track_detail["track_id"])

        # Once the user leaves pick_recommendations_loop, they either:
        #    - want to pick a brand-new track (which loops back),
        #    - or they have quit altogether.
        # The loop continues until they choose to quit inside pick_recommendations_loop.


if __name__ == "__main__":
    main()
