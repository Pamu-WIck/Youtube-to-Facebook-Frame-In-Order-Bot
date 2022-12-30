from pytube import YouTube


def Download(link):
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
    try:
        yt.download("./Video")
    except:
        print("An error has occurred")
    print("Download is completed successfully")
