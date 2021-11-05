from django.shortcuts import render

# Create your views here.
from .models import Albums


def list_albums(request):
    albums = Albums.objects.all()
    return render(request, "albums/list_albums.html",
                  {"albums": albums})




