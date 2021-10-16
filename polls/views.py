from django.shortcuts import render
import pytube

def Run(request):
    return render(request, 'Run.html')

def Download(request):
    url = request.GET.get('url')
    youtube = pytube.YouTube(url)
    audio = youtube.streams.filter(only_audio=True).first()

    audio.download()

    return render(request, 'Download.html')
