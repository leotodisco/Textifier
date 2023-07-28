from pydub import AudioSegment
import os

src = "audio.ogg"
dest = "audio.flac"


def convert():
    sound = AudioSegment.from_ogg(src)
    sound.export(dest, format = "flac")
    os.remove("audio.ogg")


