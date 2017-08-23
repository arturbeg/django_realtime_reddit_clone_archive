from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



from .views import chat_room






urlpatterns = [

   url(r'^(?P<chat_room_type>[\w-]{,50})/(?P<label>[\w-]{,50})/$', chat_room, name='chatroom'),

    #url(r'^hello/$', chat_room, name='chatroom'),



]