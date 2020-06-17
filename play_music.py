import vlc

class Song:
    def __init__(self, song_id, name, filename):
        self.id = song_id
        self.name = name
        self.filename = filename

SPIDER = "/home/pi/Downloads/spider.mp3"
HOPES = "/home/pi/Downloads/hopes.mp3"
SONGS = [
    Song(2, "Spider Dance", SPIDER),
    Song(3, "Hopes and Dreams", HOPES)
]

#p = vlc.MediaPlayer(SPIDER)
#p.play()

from pygame import mixer

mixer.init()

#mixer.music.load(SPIDER)
#mixer.music.play()

class Jukebox:
    SONG_DB = {s.id: s for s in SONGS}
    def __init__(self):
        self.playing = None
    
    def get_song(self, song_id):
        new_song = self.SONG_DB[song_id]
        return new_song
    
    def switch_to(self, song_id):
        if self.playing:
            if song_id != self.playing:
                mixer.music.fadeout(2*1000)
            else:
                return False
        self.playing = song_id
        new_song = self.get_song(song_id)
        mixer.music.load(new_song.filename)
        mixer.music.play(loops=-1)
    
        