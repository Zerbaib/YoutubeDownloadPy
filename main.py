from fileinput import filename
from pytube import YouTube

link = input("Met le lien de la video:")
yt = YouTube(link)

downloader = yt.streams.get_highest_resolution()
print("en telechargement")

downloader.download(filename="YTBvideo.mp4")
print("fini")