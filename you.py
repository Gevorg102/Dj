import pytube


url = 'https://www.youtube.com/watch?v=cjny7ykmcUE&ab_channel=NEFFEX'

youtube = pytube.YouTube(url)
audio = youtube.streams.filter(only_audio=True).first()

audio.download()
