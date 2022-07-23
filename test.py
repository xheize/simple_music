# it's test code page
import librosa

audio_file = "./gdle_TOMBOY.mp3"

y, sr = librosa.load(audio_file)

print(y)
print(sr)

with open(audio_file, "r") as music:
    y, sr = librosa.load(music)
    print(y)
    print(sr)


