# Download-youTube-videos
This Python script utilizes the pytube library to download the highest resolution video from a specified YouTube link.

The script begins by importing the necessary module, YouTube, from the pytube library.

It assigns a YouTube link to the variable link, indicating the URL of the video to be downloaded.

The script then creates a YouTube object, youtube_1, based on the provided link.

It uses the get_highest_resolution() function to retrieve the stream with the highest resolution available for the video.

The script proceeds to download the video using the download() function associated with the video_stream object.

Once the download is complete, it prints "Download complete" to the console, indicating that the download process has finished successfully.
