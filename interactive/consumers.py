import re
import json
from channels import Group
from chats.models import GlobalChat, LocalChat, Topic
from django.contrib.auth.models import User
#from channels.auth import channel_session_user, channel_session_user_from_http
from channels.sessions import channel_session
from chats.models import Topic, LocalChat, GlobalChat
from interactive.models import Message





# Connected to chat-messages, implement later

#def msg_consumer(message):
    # Save to model




# Connected to websocket.connect

@channel_session
def ws_connect(message):




    print("The ws_add is called")

    list = message['path'].strip('/').split('/')
    print(list)
    prefix = list[0]
    room_type = list[1]
    room_label = list[2]

    print('The prefix is ' + prefix)
    print('room_type is ' + room_type)
    print('The label is ' + room_label)


    if prefix!='m':
        print("The prefix has to be m to access the chat room")



    print("Pulling the chat room out of the database")

    if room_type == "topic":
        room = Topic.objects.get(label=room_label)
        print('the topic has been received, its name is ' + room.name)

    elif room_type == "localchat":
        room = LocalChat.objects.get(label=room_label)
        print('the localchat has been created')

    elif room_type == "globalchat":
        room = GlobalChat.objects.get(label=room_label)
        print('the globalchat has been created')




    # Accept the incoming connection
    message.reply_channel.send({"accept": True})

    message.channel_session['room_label'] = room.label
    print('Channel session - room label ' + message.channel_session['room_label'])

    message.channel_session['room_type'] = room_type

    print('Channel session - room type ' + message.channel_session['room_type'])

    Group('m-' + room_type + room_label, channel_layer=message.channel_layer).add(message.reply_channel)


    print("The execution of the ws_add is completed --------")





# Connected to websocket.receive
@channel_session
def ws_receive(message):
    # ASGI WebSocket packet-received and send-packet message type
    # both have a text ket fort ehri textual data

    print("The ws_message is called")

    room_type = message.channel_session['room_type']
    print(room_type + " received")
    room_label = message.channel_session['room_label']
    print(room_label + " received")


    data = json.loads(message['text'])

    if room_type == "topic":
        room = Topic.objects.get(label=room_label)
        m = room.topic_messages.create(text=data['text'], user=User.objects.get(id=1))  # need to finish editing
        print('the message is here')
        print(m)

    elif room_type == "localchat":
        room = LocalChat.objects.get(label=room_label)
        m = room.topic_messages.create(text=data['text'], user=User.objects.get(id=1))

    elif room_type == "globalchat":
        room = GlobalChat.objects.get(label=room_label)
        m = room.topic_messages.create(text=data['text'], user=User.objects.get(id=1))

    Group('m-' + room_type + room_label, channel_layer=message.channel_layer).send({'text': json.dumps(m.as_dict())})













# Connected to websocket.disconnect

@channel_session
def ws_disconnect(message):
    print("The ws_disconnect is called")

    room_label = message.channel_session['room_label']
    room_type = message.channel_session['room_type']

    print(room_type + "  " + room_label)
    print('Disconnecting...')




    if room_type == "topic":
        room = Topic.objects.get(label=room_label)

    elif room_type == "localchat":
        room = LocalChat.objects.get(label=room_label)

    elif room_type == "globalchat":
        room = GlobalChat.objects.get(label=room_label)

    Group('m-' + room_type + room_label).discard(message.reply_channel)

    Group('m-' + room_type + room_label, channel_layer=message.channel_layer).discard(message.reply_channel)













































'''
def http_consumer(message):
    response = HttpResponse("Hello world, you asksed for %s" % message.content['path'])
    # Encode the response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)







log = logging.getLogger(__name__)




@channel_session
def ws_connect(message):



    # Extract the room from the message. This expects message.path to be of the
    # form /m/{room_type}/{label   }, and finds a Room if the message path is applicable,
    # and if the Room exists. Otherwise, bails (meaning this is a some othersort
    # of websocket). So, this is effectively a version of _get_object_or_404.


    try:
        list = message['path'].strip('/').split('/')
        print(list)
        prefix = list[0]
        room_type = list[1]
        label = list[2]

        print('The prefix is ' + prefix)
        print('room_type is ' + room_type)
        print('The label is ' + label)
        print('Connecting')



        if prefix != 'm':
            print('The prefix is not m')
            return




        if room_type == "topic":
            room = Topic.objects.get(label=label)
            print('the topic has been received, its name is')

        elif room_type == "localchat":
            room = LocalChat.objects.get(label=label)
            print('the localchat has been created')

        elif room_type == "globalchat":
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

    message.channel_session['room_type'] = room_type

    print('Channel session 2 ' + message.channel_session['room_type'])

    Group('m-' + room_type + label, channel_layer=message.channel_layer).add(message.reply_channel)

    print('---')




















@channel_session
def ws_receive(message):


    try:
        room_type = message.channel_session['room_type']
        print(room_type + " received")
        label = message.channel_session['room_label']
        print(label + " received")


        #print(label)
        #print(room_type)


        # Parse out a chat message from the content text, bailing if it doesn't
        # conform to the expected message format.

        data = json.loads(message['text'])
        print("The data at the websocket has been received, it is " + data)
        #print(data)

        if room_type == "topic":
            room = Topic.objects.get(label=label)
            m = room.topic_messages.create(text = data['text'], user=User.objects.get(id=1)) # need to finish editing
            print('the message is ' + m)

        elif room_type == "localchat":
            room = LocalChat.objects.get(label=label)
            m = room.topic_messages.create(text=data['text'], user=User.objects.get(id=1))

        elif room_type == "globalchat":
            room = GlobalChat.objects.get(label=label)
            m = room.topic_messages.create(text=data['text'], user=User.objects.get(id=1))
    except KeyError:
        log.debug('no room in channel session')
        return

    # add except RoomDoesNotExist later







    Group('m-' + room_type + label, channel_layer=message.channel_layer).send({'text': json.dumps(m.as_dict())}) # Group.send() will take care of sending this message to every reply_channel added to the group.






@channel_session
def ws_disconnect(message):

    try:
        label = message.channel_session['room_label']
        room_type = message.channel_session['room_type']

        print(room_type +  "  " + label)
        print('Disconnecting...')


        if room_type == "topic":
            room = Topic.objects.get(label=label)

        elif room_type == "localchat":
            room = LocalChat.objects.get(label=label)

        elif room_type == "globalchat":
            room = GlobalChat.objects.get(label=label)




        Group('m-' + room_type + label).discard(message.reply_channel)

    except KeyError:
        pass

'''

# Group.send() will take care of sending this message to every reply_channel added to the group.




'''

Group("chat-%s-%s" % room_type, room_label).send({

    "text": json.dumps({
        "text": message["text"],
        "username": message.channel_session["username"]
    }),
})

'''

'''
  # Parse the query string

  params = parse_qs(message.content["query_string"])
  print("The query string is parsed: " + params)

  if b"username" in params:
      # Set the username in the session
      message.channel_session["username"] = params[b"username"][0].decode("utf8")
      # Add the user to the group

      Group("chat-%s-%s" % room_type, room_label).add(message.reply_channel)
  else:
      # Close the connection
      message.reply_channel({"close": True})

  '''