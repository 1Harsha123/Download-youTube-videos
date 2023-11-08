# from pytube import YouTube

# link="https://www.youtube.com/watch?v=x5kKXnarFUw"
# youtube_1=YouTube(link)
# videos=youtube_1.streams
# print("download complete")

from pytube import YouTube

link = "https://www.youtube.com/watch?v=x5kKXnarFUw"
youtube_1 = YouTube(link)
video_stream = youtube_1.streams.get_highest_resolution()

video_stream.download()
print("Download complete")
