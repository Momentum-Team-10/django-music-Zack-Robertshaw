from types import GetSetDescriptorType
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Albums
from .forms import AlbumForm



def list_albums(request):
    albums = Albums.objects.all()
    return render(request, "albums/list_albums.html",
                  {"albums": albums})


def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/add_album.html", {"form": form})             



