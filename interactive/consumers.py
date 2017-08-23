import re
import json
import logging
from channels import Group
from channels.sessions import channel_session
from chats.models import GlobalChat, LocalChat, Topic
from django.contrib.auth.models import User



log = logging.getLogger(__name__)




@channel_session
def ws_connect(message):



    # Extract the room from the message. This expects message.path to be of the
    # form /m/{chat_room_type}/{label   }, and finds a Room if the message path is applicable,
    # and if the Room exists. Otherwise, bails (meaning this is a some othersort
    # of websocket). So, this is effectively a version of _get_object_or_404.


    try:
        list = message['path'].strip('/').split('/')
        print(list)
        prefix = list[0]
        chat_room_type = list[1]
        label = list[2]

        print('The prefix is ' + prefix)
        print('chat_room_type is ' + chat_room_type)
        print('The label is ' + label)
        print('Connecting')



        if prefix != 'm':
            print('The prefix is not m')
            return




        if chat_room_type == "topic":
            room = Topic.objects.get(label=label)
            print('the topic has been received, its name is')

        elif chat_room_type == "localchat":
            room = LocalChat.objects.get(label=label)
            print('the localchat has been created')

        elif chat_room_type == "globalchat":
            room = GlobalChat.objects.get(label=label)
            print('the globalchat has been created')

    except ValueError:
        print('There is a Value error')
        return

    # Add room does not exist later




    print('Making the Group')

    # start from debugging this section
    print(message.channel_session)

    message.channel_session['room_label'] = room.label
    print('Channel session 1 ' + message.channel_session['room_label'])


    #message.channel_session['room_label'] = label
    #print(message.channel_session['room_label'])

    message.channel_session['room_type'] = chat_room_type

    print('Channel session 2 ' + message.channel_session['room_type'])

    Group('m-' + chat_room_type + label, channel_layer=message.channel_layer).add(message.reply_channel)

    print('---')




















@channel_session
def ws_receive(message):


    try:
        chat_room_type = message.channel_session['room_type']
        print(chat_room_type + " received")
        label = message.channel_session['room_label']
        print(label + " received")


        #print(label)
        #print(chat_room_type)


        # Parse out a chat message from the content text, bailing if it doesn't
        # conform to the expected message format.

        data = json.loads(message['text'])
        print("The data at the websocket has been received, it is " + data)
        #print(data)

        if chat_room_type == "topic":
            room = Topic.objects.get(label=label)
            m = room.topic_messages.create(text = data['text'], user=User.objects.get(id=1)) # need to finish editing
            print('the message is ' + m)

        elif chat_room_type == "localchat":
            room = LocalChat.objects.get(label=label)
            m = room.topic_messages.create(text=data['text'], user=User.objects.get(id=1))

        elif chat_room_type == "globalchat":
            room = GlobalChat.objects.get(label=label)
            m = room.topic_messages.create(text=data['text'], user=User.objects.get(id=1))
    except KeyError:
        log.debug('no room in channel session')
        return

    # add except RoomDoesNotExist later







    Group('m-' + chat_room_type + label, channel_layer=message.channel_layer).send({'text': json.dumps(m.as_dict())}) # Group.send() will take care of sending this message to every reply_channel added to the group.






@channel_session
def ws_disconnect(message):

    try:
        label = message.channel_session['room_label']
        chat_room_type = message.channel_session['room_type']

        print(chat_room_type +  "  " + label)
        print('Disconnecting...')


        if chat_room_type == "topic":
            room = Topic.objects.get(label=label)

        elif chat_room_type == "localchat":
            room = LocalChat.objects.get(label=label)

        elif chat_room_type == "globalchat":
            room = GlobalChat.objects.get(label=label)




        Group('m-' + chat_room_type + label).discard(message.reply_channel)

    except KeyError:
        pass

