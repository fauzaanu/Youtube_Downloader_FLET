# a program to download a YouTube video in the highest quality
# for my own personal use only
from pytube import YouTube


class YoutubeDL:
    # define file size here and update it from inside
    filesize = int()
    progress_amount = int()

    def __init__(self, link):
        # progress func.  Adapted from https://stackoverflow.com/questions/62360943/pytube-how-to-add-a-progress-bar
        def progress(chunk, file_handle, bytes_remaining):
            remaining = (100 * bytes_remaining) / YoutubeDL.filesize
            step = 100 - int(remaining)

            YoutubeDL.progress_amount = int(step)

            #print("Completed:", step)  # show the percentage of completed download

        video_obj = YouTube(link, on_progress_callback=progress)
        banned_chars = ["!", "?", "-", ":", "|", " ", "<", ">", ":", '"', '/', '\\', "+", "&", "^", "="]
        video_name = video_obj.title

        for char in banned_chars:
            # making names more clear
            video_name = video_name.replace(char, "_")
            video_name = video_name.replace("__", "_")
            video_name = video_name.replace("__", "_")
            video_name = video_name.replace("__", "_")
            video_name = video_name.replace("__", "_")

        file = video_obj.streams.get_highest_resolution()
        YoutubeDL.filesize = file.filesize
        file.download(filename=f'{video_name}.mp4')



