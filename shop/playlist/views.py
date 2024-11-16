from django.shortcuts import render, redirect
from playlist.models import Video


def playlist(request):
    videos = Video.objects.all()
    return render(request, 'playlist/playlist.html', {
        'videos': videos
    })


def video_create(request):
    if request.method == 'POST':
        Video.objects.create(
            embed_code=request.POST['embed_code'],
        )
        return redirect('playlist')
    return render(request, 'playlist/video_create.html')

def video_like(request):
    print(request.POST)
    video_id = request.POST['video_id']
    video = Video.objects.get(id=video_id)
    video.likes +=1
    video.save()
    return redirect('playlist')

