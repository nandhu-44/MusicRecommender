# 🎵 [Music Recommender](https://github.com/nandhu-44/MusicRecommender) 🎵

This project provides music genre recommendations and suggests Spotify playlists based on user input.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/nandhu-44/MusicRecommender.git
   ```

2. Change directory to the project folder:

   ```bash
   cd MusicRecommender
   ```

3. Install the required packages:

   ```bash
    pip install -r requirements.txt
   ```

4. Setup `playlists.json` file.
   - Create a new file named `playlists.json` in the project folder.
   - Add your spotify playlist links to the file in the following format:
     ```json
     {
       "genre1": ["playlist1", "playlist2", "playlist3"],
       "genre2": ["playlist1", "playlist2", "playlist3"],
       "genre3": ["playlist1", "playlist2", "playlist3"]
     }
     ```
   - Save the file.
5. Run the code:
   - Windows:
     ```bash
     python musicRecommender.py
     ```
   - Linux/Mac:
     ```bash
     python3 musicRecommender.py
     ```
