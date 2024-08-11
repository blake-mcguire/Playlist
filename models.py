class Song:
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

    def __repr__(self):
        return f"Song(name={self.name}, artist={self.artist}, genre={self.genre})"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        self.songs = [song for song in self.songs if song.name != song_name]

    def sort_songs(self, key='name'):
        if key == 'name':
            self.songs.sort(key=lambda song: song.name)
        elif key == 'artist':
            self.songs.sort(key=lambda song: song.artist)
        elif key == 'genre':
            self.songs.sort(key=lambda song: song.genre)

    def __repr__(self):
        return f"Playlist(name={self.name}, songs={self.songs})"
