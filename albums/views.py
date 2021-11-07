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


def edit_album(request, pk):
    album = get_object_or_404(Albums, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/edit_album.html", {
        "form": form,
        "album": album
    })

def delete_album(request, pk):
    album = get_object_or_404(Albums, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_album.html",
                  {"album": album})

       

# def edit_contact(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     if request.method == 'GET':
#         form = ContactForm(instance=contact)
#     else:
#         form = ContactForm(data=request.POST, instance=contact)
#         if form.is_valid():
#             form.save()
#             return redirect(to='list_contacts')

#     return render(request, "contacts/edit_contact.html", {
#         "form": form,
#         "contact": contact
#     })


