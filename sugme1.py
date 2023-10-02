import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pygame
import time
# Spotify API credentials
client_id="d20fff850e694bc28eef65b86db2f1e1"
client_secret="055fcaf0624649898c5c2f50c8c9fbd9"
redirect_uri="http://localhost:8889/callback"
                                                   
 
# Initialize the Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-library-read'))

# Get the user's saved tracks (listening history)
def get_user_saved_tracks():
    results = sp.current_user_saved_tracks()
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

# Example mood-based recommendation function
def recommend_music(user_tracks, mood):
    recommended_tracks = []
    for track in user_tracks:
        # Request audio features for the track
        track_id = track['track']['id']
        audio_features = sp.audio_features(track_id)[0]  # Assumes you have a valid track ID

        # Check if 'valence' is present in the audio features
        if 'valence' in audio_features:
            valence = audio_features['valence']
            
            # Customize mood-based criteria as needed
            if mood == 'happy' and valence > 0.7:
                recommended_tracks.append(track)
            elif mood == 'sad' and valence < 0.3:
                recommended_tracks.append(track)
    
    return recommended_tracks

# User input for mood (for simplicity)
user_mood = input("Enter your mood (happy/sad): ")

# Get user's saved tracks
user_tracks = get_user_saved_tracks()

# Recommend music based on mood
recommended_tracks = recommend_music(user_tracks, user_mood)

# Display recommended tracks
print("Recommended Tracks:")
for track in recommended_tracks:
    track_name = track['track']['name']
    artist_name = track['track']['artists'][0]['name']
    print(f"{track_name} by {artist_name}")
