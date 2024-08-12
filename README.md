# Music Playlist Management System

This project is a Music Playlist Management System built using Python and Flask. It allows users to create, manage, and organize songs and playlists. The system includes basic CRUD operations for songs and playlists and provides sorting and searching functionalities.

## Features

- **Songs Management**: Create, update, delete, and search for songs.
- **Playlists Management**: Create, update, delete, and manage playlists.
- **Sorting**: Sort songs in a playlist by name, artist, or genre.
- **Searching**: Linear and binary search functionalities to find songs.

## Project Structure

- `models.py`: Contains the `Song` and `Playlist` classes, which are used to model the songs and playlists in the system.
- `song_endpoints.py`: Contains the Flask endpoints for managing songs and playlists. Includes routes for creating, updating, deleting, and searching songs, as well as managing playlists.
- `algorithms.py`: Contains the sorting and searching algorithms used in the project, including `linear_search`, `binary_search`, and `merge_sort`.

## Installation

1. **Clone the repository:**

   git clone https://github.com/yourusername/music-playlist-management.git
   cd music-playlist-management

2. Create Virtual Enviroment and activate it

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
 
3. Install the required dependencies

    pip install Flask



## USAGE 

1. Run the flask app
  
   python yourfile.py
    
2. Access the application 
   Open your browser and access your local host  http://127.0.0.1:5000/.

## API Endpoints
### Songs

Create a song

#### POST /songs
Body: { "name": "Song Name", "artist": "Artist Name", "genre": "Genre" }
Update a song

#### PUT /songs/<name>
Body: { "name": "New Song Name", "artist": "New Artist Name", "genre": "New Genre" }
Delete a song

DELETE
 /songs/<name>

Search for songs

    GET /songs/search?query=<query>&key=<key>
    Query Parameters:
        query: The search term.
        key: The attribute to search by (name, artist, or genre).

### Playlists

### Create a playlist

    POST /playlists
        Body: { "name": "Playlist Name" }

### Get a playlist

    GET /playlists/<name>

### Update a playlist

    PUT /playlists/<name>
    Body: { "name": "New Playlist Name" }

### Delete a playlist

DELETE /playlists/<name>

### Add a song to a playlist

    POST /playlists/<name>/add_song
        Body: { "song_name": "Song Name" }
    
### Remove a song from a playlist

    POST /playlists/<name>/remove_song
        Body: { "song_name": "Song Name" }

### Sort songs in a playlist

    GET /playlists/<name>/sort?key=<key>
        Query Parameters:
        key: The attribute to sort by (name, artist, or genre).

## Algorithms
### Linear Search: Searches for songs based on the provided key.
### Binary Search: Efficiently searches for songs in a sorted list.
### Merge Sort: Sorts the songs in a playlist based on the specified key.