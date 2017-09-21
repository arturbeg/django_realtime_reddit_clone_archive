from django.shortcuts import render, get_object_or_404
from .models import Message
from chats.models import Topic, LocalChat, GlobalChat, ChatGroup
from django.shortcuts import render, redirect
from django.views.generic import RedirectView, DetailView
from chats.forms import TopicUpdateForm, LocalChatCreateForm
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q
from django.http import HttpResponse
import json
from django.views.decorators.csrf import ensure_csrf_cookie



def like_a_message(request):
    print("Ajax liking a message........")
    if request.method == 'POST':
        user = request.user
        message_id = request.POST.get('message_id')
        message = get_object_or_404(Message, id=message_id)

        if message.likers.filter(id=user.id).exists():
            # user has already liked this company
            # remove like/user
            message.likers.remove(user)
            print("You removed your like")
        else:
            # add a new like for a company
            message.likers.add(user)
            print("You liked this")

    context = {'likes_count': message.get_number_of_likes(), 'message_id': message_id}

    return HttpResponse(json.dumps(context), content_type='application/json')



def search_chat_room(request):

    print("Ajax Searching Chat Rooms..........")
    query = request.GET.get('q')
    print(query)
    modelToSearch = request.GET.get('modelToSearch')
    print(modelToSearch)
    chatgroup_id = request.GET.get('chatgroup_id')
    print(chatgroup_id)
    is_localchat = modelToSearch == 'localChat'
    print(is_localchat)

    if query is not None and query != '' and request.is_ajax():

        if modelToSearch == "localChat":
            results = LocalChat.objects.filter(
                Q(name__icontains=query) & Q(chatgroup__id=chatgroup_id)
            )

            print(results)
        else:
            results = Topic.objects.filter(

                Q(name__icontains=query) & Q(chatgroup=chatgroup_id)
            )
            print(results)


        return render(
            request, 'interactive/results.html',
            {'results': results, 'is_localChat': is_localchat}
        )
    return render(
        request, 'interactive/results.html', {'is_localChat': is_localchat}
    )

'''
def chat_room_search(request):
    if request.is_ajax():
        q = request.GET.get('q')
        model = request.GET.get('modelToSearch')
        print(model)
        is_localchat = model == 'localChat'
        #print(is_localchat)



        if q is not "":
            if model == 'localChat':
                results = LocalChat.objects.filter(
                    Q(name__icontains=q))
            else:
                results = Topic.objects.filter(
                    Q(name__icontains=q))

                print(results)







            return render(request, 'interactive/results.html', {'results': results, 'is_localchat': is_localchat})



'''



@ensure_csrf_cookie
def chat_room(request, label, chat_room_type):

    if chat_room_type == "topic":
        room, created = Topic.objects.get_or_create(label=label)
        messages = reversed(room.topic_messages.order_by('-timestamp')[:5])
        print('The name of the room is' +  room.name)
        print("All the messages of that room have been established")

    elif chat_room_type == "localchat":
        room, created = LocalChat.objects.get_or_create(label=label)
        messages = reversed(room.localchat_messages.order_by('-timestamp')[:5 ])
    elif chat_room_type == "globalchat":
        room, created = GlobalChat.objects.get_or_create(label=label)
        messages = reversed(room.globalchat_messages.order_by('-timestamp')[:5])
    else:
        print("A valid chat room type has not been provided")





    # Implement search here -- will use another fucntion to implement search

    list_of_localchats = room.chatgroup.localchat_set.all()


    list_of_topics = room.chatgroup.topic_set.all()






    # Now need to get the most liked message in the localchat


    chatgroup = room.chatgroup.name

    is_owner = request.user.id == room.get_owner()
    print(is_owner)




    # Settings of the room -> changes made to the chatroom







    if request.method == "POST":

        if chat_room_type == "topic":
            print("IT IS A TOPIC ----------------")
            form = TopicUpdateForm(request.POST, request.FILES)
        elif chat_room_type == "localchat":
            print("IT IS A LOCAL CHAT -----------")
            form = LocalChatCreateForm(request.POST, request.FILES)


        if form.is_valid():

            print(room.name)

            chatgroup_id = room.chatgroup.id


            # updateRoom is the same object as the room since it has the same id, have to do it because the form does not
            # contain all the necessary fields, otherwise a new instance is created

            updatedRoom = form.save(commit=False)

            updatedRoom.chatgroup = ChatGroup.objects.get(id=chatgroup_id)

            updatedRoom.id = room.id

            updatedRoom.label = room.label

            updatedRoom.timestamp = room.timestamp

            if not updatedRoom.avatar: # If the user does not put anything for the avatar, we assign the old one
                updatedRoom.avatar = room.avatar



            updatedRoom.save()


            return HttpResponseRedirect(room.get_absolute_url())























    return render(request, "interactive/room.html", context = {
        'chatgroup': chatgroup,
        'chat_room_type': chat_room_type,
        'room': room,
        'messages': messages,
        'localchats': list_of_localchats,
        'is_owner': is_owner,
        'topics': list_of_topics,
        #'form': form,
    })


















'''
class MessageLikeRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        label = self.kwargs.get("label")

        user = self.request.user

        if user.is_authenticated():

        return

'''











'''
    for localchat in list_of_localchats:

        list_of_messages = localchat.localchat_messages.order_by('-timestamp')[:1]


        if len(list_of_messages) == 0:
            print("There is no messages in the local chat")
            top_message = "There are no messages in this localchat"

        else:
            top_message = list_of_messages[0]
            print(top_message.text)



        print(localchat.name)

    '''


'''

    Show the room, with latest messages.
    The template for this view has the WebSocket business to send and stream messages,
    so see the template for where the magic happens.

    '''
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).