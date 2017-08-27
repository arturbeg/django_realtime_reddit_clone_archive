from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve



from .views import chat_room






urlpatterns = [

   url(r'^(?P<chat_room_type>[\w-]{,50})/(?P<label>[\w-]{,50})/$', chat_room, name='chatroom'),

   # In the case of a global chat, the chat_room_type is globalchat and the label is just the
   # chatgroup label
   #url(r'^(?P<chat_room_type>[\w-]{,50})/(?P<label>[\w-]{,50})/media/(?P<path>.*)$', serve, {
    #        'document_root': settings.MEDIA_ROOT,
     #  })


    #url(r'^hello/$', chat_room, name='chatroom'),



]


#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# work out the deal with the media files

