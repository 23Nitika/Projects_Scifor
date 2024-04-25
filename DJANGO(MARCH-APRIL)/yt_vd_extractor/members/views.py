from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from pytube import *

# defining function 
def youtube(request): 
  
    if request.method == 'POST': 
        
        link = request.POST['link'] 
        video = YouTube(link) 

        stream = video.streams.get_lowest_resolution() 
          
        stream.download() 
  
        # returning HTML page 
        return render(request, 'youtube.html', {'video_downloaded': True}) 
    return render(request, 'youtube.html')