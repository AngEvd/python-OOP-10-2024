from project.song import Song
from typing import Tuple


class Album:
    def __init__(self, name: str, *songs: Tuple[Song]) -> None:
        self.name = name
        self.songs = [*songs]
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        else:
            return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self) -> str:
        song_details = "\n".join(f"== {song.get_info()}" for song in self.songs)
        return f"Album {self.name}\n{song_details}\n"
