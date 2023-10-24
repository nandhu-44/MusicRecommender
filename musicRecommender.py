import joblib
import warnings
import random
import json


def main():
    warnings.filterwarnings("ignore", category=UserWarning)
    model = joblib.load('musicRecommender.bin')
    playlists = json.load(open('playlists.json'))

    def get_spotify_playlist(playlists, predicted_genre):
        return random.choice(playlists[predicted_genre])

    print("--------------------Music Recommender--------------------")
    try:
        age = int(input("Enter your age : "))
        gender = input("Enter your gender (m/f) : ").strip().lower()
    except ValueError:
        print("Provide a valid age!")
        exit()

    if gender in ["male", "m"]:
        gender_int = 1
    elif gender in ["female", "f"]:
        gender_int = 0
    else:
        print("Provide a valid gender! (Male/Female)")
        exit()

    user_data = [[age, gender_int]]
    predicted_genre = model.predict(user_data)[0]

    print(f"Music Genre Suggestion: {predicted_genre}")
    suggested_playlist = get_spotify_playlist(playlists, predicted_genre)
    print(
        f"Spotify Playlist: https://open.spotify.com/playlist/{suggested_playlist}")


if __name__ == "__main__":
    main()
