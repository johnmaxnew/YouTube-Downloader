from pytube import YouTube

while True:
    link = input("enter url: ") 
    video = YouTube(link)
    for stream in video.streams.filter(only_audio = True, mime_type = "audio/mp4"):
        stream = video.streams.get_by_itag(140)
        stream.download(output_path="Your directory here e.g '/Users/ADMIN/Desktop/music' ")
    print("done")
    
