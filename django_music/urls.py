"""django_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from albums import views as albums_views
# import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', albums_views.list_albums, name='list_albums'),
    path('albums/add_album/', albums_views.add_album, name='add_album'),
    path('albums/<int:pk>/edit_album/',
         albums_views.edit_album,
         name='edit_album'),
    path('albums/<int:pk>/delete_album/',
         albums_views.delete_album,
         name='delete_album'),



]
    # path('__debug__/', include(debug_toolbar.urls)),


"""
| path                      | verb | purpose                                               |
| ------------------------- | ---- | ----------------------------------------------------- | 
| `""`                      | GET  | show a list of all the albums                         |
| `/albums/new`             | GET  | show a form to create a new album                     |
| `/albums/new`             | POST | create a new album                                    |
| `/albums/<int:pk>`        | GET  | show details about a single album                     |
| `/albums/<int:pk>/edit`   | GET  | show a form to edit a new album                       |
| `/albums/<int:pk>/edit`   | POST | update a specific album                               |
| `/albums/<int:pk>/delete` | GET  | show a confirmation screen to delete a specific album |
| `/albums/<int:pk>/delete` | POST | delete a specific album                              

"""


    # path('contacts/add/', contacts_views.add_contact, name='add_contact'),


# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),

#         # For django versions before 2.0:
#         # url(r'^__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
