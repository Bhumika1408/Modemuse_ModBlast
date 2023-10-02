import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import pygame
import io
from concurrent.futures import ThreadPoolExecutor

# Initialize Spotify API client
client_id="d20fff850e694bc28eef65b86db2f1e1"
client_secret= "055fcaf0624649898c5c2f50c8c9fbd9"
redirect_uri='http://localhost:8889/callback'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope='user-library-read'
))

# Function to categorize and play music
def categorize_and_play_music():
    # Get user's saved tracks
    results = sp.current_user_saved_tracks()
    user_tracks = results['items']

    # Define mood categories based on audio features
    mood_categories = {
        'happy': {'valence': (0.6, 1.0), 'energy': (0.7, 1.0), 'danceability': (0.7, 1.0)},
        'sad': {'valence': (0.0, 0.3), 'energy': (0.0, 0.4), 'danceability': (0.2, 0.5)},
        'excited': {'valence': (0.7, 1.0), 'energy': (0.7, 1.0), 'danceability': (0.7, 1.0)},
        'neutral': {'valence': (0.4, 0.6), 'energy': (0.4, 0.6), 'danceability': (0.4, 0.6)}
    }

    categorized_tracks = {mood: [] for mood in mood_categories}

    # Categorize tracks
    for track in user_tracks:
        track_id = track['track']['id']
        audio_features = sp.audio_features(track_id)[0]
        if audio_features:
            valence = audio_features['valence']
            energy = audio_features['energy']
            danceability = audio_features['danceability']
            for mood, conditions in mood_categories.items():
                valence_range = conditions['valence']
                energy_range = conditions['energy']
                danceability_range = conditions['danceability']
                if (
                    valence_range[0] <= valence <= valence_range[1] and
                    energy_range[0] <= energy <= energy_range[1] and
                    danceability_range[0] <= danceability <= danceability_range[1]
                ):
                    categorized_tracks[mood].append(track)

    # Play categorized tracks
    for mood, tracks in categorized_tracks.items():
        if tracks:
            print(f"{mood.capitalize()} Tracks:")
            for idx, track in enumerate(tracks):
                track_name = track['track']['name']
                artist_name = track['track']['artists'][0]['name']
                print(f"{idx + 1}. {track_name} by {artist_name}")

            choice = int(input(f"Enter the {mood} track number you want to play (or 0 to skip): "))
            if 0 < choice <= len(tracks):
                track = tracks[choice - 1]['track']
                play_track(track)
            else:
                print(f"Skipping {mood} tracks.")

def play_track(track):
    track_id = track['id']
    
    # Check if 'preview_url' is available
    track_info = sp.track(track_id)
    if 'preview_url' in track_info and track_info['preview_url']:
        track_stream_url = track_info['preview_url']
        
        # Download the audio
        response = requests.get(track_stream_url)
        audio_data = io.BytesIO(response.content)
        
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Load and play the audio
        pygame.mixer.music.load(audio_data)
        pygame.mixer.music.play()
        
        # Wait for the track to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
        print("No preview URL available for this track.")

# Run the categorization and playback
categorize_and_play_music()
