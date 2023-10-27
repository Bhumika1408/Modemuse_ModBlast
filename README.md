<p align="center">
  <img src="your_repository_logo.png" alt="Repository Logo">
</p>

# Mood-Based Music Recommendation with Spotify 🎵🎶

### Description

This repository 📦 contains a Python project that utilizes the Spotify API for mood-based music recommendation. The project consists of two main Python files and is designed to provide personalized music recommendations based on the user's mood. 🎉 Here's an overview of the key components and features of this repository:


- **Authentication:** The `main.py` script initializes the Spotify API client using your Spotify credentials, including the client ID, client secret, and a redirect URI. It authenticates the application with the Spotify API, ensuring secure access to the user's Spotify account and saved tracks.

- **Mood-Based Music Recommendation:** The script categorizes the user's saved tracks into different mood categories based on their audio features, such as valence, energy, and danceability. Users can specify their current mood (e.g., "happy," "sad," "excited," or "neutral"), and the script recommends tracks that match the mood criteria.

- **Interactive User Experience:** The user can interact with the script by selecting a track to play from each mood category. Pygame is used for audio playback, allowing users to listen to their chosen tracks.


**Features:**

- **Custom Mood Selection:** Users can input their mood, allowing for a personalized music listening experience based on their emotional state.

- **Categorized Playlists:** The script categorizes saved tracks into mood categories, making it easier for users to explore and play tracks that match their desired mood.

- **Audio Playback:** It provides the ability to play selected tracks directly within the application using Pygame for audio playback.

**Dependencies:**

- Python 3.x 🐍
- Spotipy library for Spotify API integration 🎵
- Pygame for audio playback 🕹️
- Requests library for making HTTP requests 📡
- Concurrent Futures for parallel execution (ThreadPoolExecutor) ⚡

**How to Use:**

1. Clone the repository to your local machine 📁.
2. Make sure you have the required dependencies installed 🛠️.
3. Configure your Spotify API credentials (client ID, client secret, and redirect URI) in the `main.py` script 🔑.
4. Run the `main.py` script to start the application 🚀.
5. Follow the prompts to authenticate, select your mood, and explore and play recommended tracks 🎶.

**Usage Scenario:**

This project is ideal for music enthusiasts who want a more personalized and mood-aligned listening experience. It simplifies the process of finding and enjoying music that matches your current emotional state, whether you're looking to uplift your mood, relax, or simply explore new tracks that resonate with your feelings. 🌟

Feel free to explore the code, customize mood criteria, and extend the functionality to suit your preferences and needs. 🎨👨‍💻

</div>
