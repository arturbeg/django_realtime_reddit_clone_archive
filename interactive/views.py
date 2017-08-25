from django.shortcuts import render
from .models import Message
from chats.models import Topic, LocalChat, GlobalChat, ChatGroup
from django.contrib.auth.models import User

import random
import string
from django.db import transaction
from django.shortcuts import render, redirect
#import haikunator









def chat_room(request, label, chat_room_type):




    '''

    Show the room, with latest messages.
    The template for this view has the WebSocket business to send and stream messages,
    so see the template for where the magic happens.

    '''
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).


    if chat_room_type == "topic":
        room, created = Topic.objects.get_or_create(label=label)
        messages = reversed(room.topic_messages.order_by('-timestamp')[:50])
        print('The name of the room is' +  room.name)
        print("All the messages of that room have been established")
    elif chat_room_type == "localchat":
        room, created = LocalChat.objects.get_or_create(label=label)
        messages = reversed(room.localchat_messages.order_by('-timestamp')[:50])
    elif chat_room_type == "globalchat":
        room, created = GlobalChat.objects.get_or_create(label=label)
        messages = reversed(room.globalchat_messages.order_by('-timestamp')[:50])
    else:
        print("A valid chat room type has not been provided")

    # We want to show the last 50 messages, ordered most-recent-last


    chatgroup = room.chatgroup.name
    profile = request.user.profile
    print("prpofile is here")
    print(profile)


    return render(request, "interactive/room.html", {
        'chatgroup': chatgroup,
        'chat_room_type': chat_room_type,
        'room': room,
        'messages': messages,
        'profile': profile,
    })

