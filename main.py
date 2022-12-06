from fileinput import filename
from pytube import YouTube

link = input("Met le lien de la video:\n")
format = input("En quoi le veux tu: (1 - mp3) (2 - mp4)")
yt = YouTube(link)

def mp3():
    downloader.download(filename="YTBvideo.mp3")
def mp4():
    downloader.download(filename="YTBvideo.mp4")

downloader = yt.streams.get_highest_resolution()
print("en telechargement")

if format == "1":
    mp3()
else:
    mp4()

print("fini")