from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from .forms import ChatGroupCreateForm, TopicCreateForm, LocalChatCreateForm
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, ChatGroup, Topic, LocalChat, GlobalChat
from django.http import Http404
from django.views.generic.edit import FormMixin
from django.urls import reverse
from interactive.models import Post
import operator
from django.db.models import Q

from functools import reduce







def chargroup_search_list(request):
    template = 'chats/chatgroup_search.html'
    queryset = ChatGroup.objects.all()

    query = request.GET.get('q')
    if query:
        result = queryset.filter(

            Q(name__icontains=query) |
            Q(about__icontains=query)

        )






    context = {"objects": result}
    return render(request, template, context)








'''class ChatgroupSearchList(ListView):

    model = ChatGroup
    template = 'chats/chatgroup_search.html'''




class ProfileDetail(DetailView):
    model = Profile
    template_name = 'chats/profile.html'

    def get_context_data(self, **kwargs):
        print("Updating the get_context_data method")
        data = super(ProfileDetail, self).get_context_data(**kwargs)
        self.object = self.get_object()
        print(self.object.user.id)

        chatgroups = ChatGroup.objects.filter(members__id=self.object.user.id)

        print(chatgroups)

        data['chatgroups'] = chatgroups



        posts = Post.objects.filter(message__user__id = self.object.user.id)
        print(posts)

        data['posts'] = posts

        return data


class ChatGroupDetailView(FormMixin, DetailView):
    model = ChatGroup
    template_name = 'chats/chatgroupdetail.html'
    form_class = LocalChatCreateForm

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('chatgroup-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        data = super(ChatGroupDetailView, self).get_context_data(**kwargs)
        data['form'] = self.get_form()
        print(self.request.user.id)
        self.object = self.get_object()
        print(self.object.owner.id)

        is_owner = self.object.owner.id == self.request.user.id
        print(is_owner)

        data['is_owner'] = is_owner


        chatgroup_topics = Topic.objects.filter(chatgroup__id = self.object.id)

        data['topics'] = chatgroup_topics

        return data

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.chatgroup = self.get_object()
        instance.save()


        return super(ChatGroupDetailView, self).form_valid(form)


class TrendingLocalChatsList(ListView):
    model = LocalChat
    template_name = 'chats/trending_localchats_list.html'


    def get_queryset(self):

        if self.request.user.is_authenticated:

            queryset = LocalChat.objects.all()
            print(queryset)
            chatgroups_followed = self.request.user.is_member.all()
            print(chatgroups_followed)

            for localchat in queryset:
                print(localchat)
                chatgroups_counter = chatgroups_followed.count()

                for chatgroup in chatgroups_followed:
                    if localchat not in chatgroup.localchat_set.all():
                        chatgroups_counter -= 1
                print(chatgroups_counter)

                if chatgroups_counter == 0:
                    queryset = queryset.exclude(name = localchat.name)


        else:
            print("The user is not authenticated")
            queryset = LocalChat.objects.all()


        print(queryset)








        return queryset



def profile_followers(request, pk, *args, **kwargs):
    template_name = "chats/profile_followers.html"
    profile = Profile.objects.get(pk=pk)
    print(profile.user.username)

    queryset = profile.followers.all()
    print(queryset)

    c = {"followers" : queryset}
    return render(request, template_name, c)




def profile_following(request, pk, *args, **kwargs):
    template_name = "chats/profile_following.html"
    profile = Profile.objects.get(pk=pk)

    queryset = profile.user.is_following.all()
    print(queryset)

    c = {"following": queryset}
    return render(request, template_name, c)





def profile_chatgroups(request, pk, *args, **kwargs):
    template_name = "chats/profile_chatgroups.html"
    profile = Profile.objects.get(pk=pk)

    queryset = ChatGroup.objects.filter(members__id=profile.user.id)

    c = {"chatgroups": queryset}
    return render(request, template_name, c)










    '''
    def get_queryset(self):
        chatgroups = self.request.user.is_member.all()
        queryset = LocalChat.objects.all() # initial unmodified queryset

        print('The user is ' + str(self.request.user))
        print(chatgroups)


        for localchat in queryset:
            for chatgroup in chatgroups:
                if localchat not in chatgroup.localchat_set.all():
                    queryset = queryset.exclude(name = localchat.name)
        print(queryset)



        return queryset
        '''




class TrendingGlobalChatsList(ListView):
    model = GlobalChat
    template_name = 'chats/trending_globalchats_list.html'



    def get_queryset(self):

        if self.request.user.is_authenticated:

            queryset = GlobalChat.objects.all()
            print(queryset)
            chatgroups_followed = self.request.user.is_member.all()
            print(chatgroups_followed)

            for globalchat in queryset:
                print(globalchat)
                globalchat_chatgroup = globalchat.chatgroup

                chatgroups_counter = chatgroups_followed.count()

                for chatgroup in chatgroups_followed:
                  if chatgroup.id != globalchat_chatgroup.id:
                     chatgroups_counter -= 1
                print(chatgroups_counter)

                if chatgroups_counter == 0:
                    queryset = queryset.exclude(label=globalchat.label)

        else:
            print("The use is not authenticated")

            queryset = GlobalChat.objects.all()


        print(queryset)

        return queryset










class TrendingTopicsList(ListView):
    model = Topic
    template_name = 'chats/trendingtopicslist.html'

    def get_queryset(self):


        if self.request.user.is_authenticated:


            queryset = Topic.objects.all()
            print(queryset)
            chatgroups_followed = self.request.user.is_member.all()
            print(chatgroups_followed)

            for topic in queryset:
                print(topic)
                chatgroups_counter = chatgroups_followed.count()

                for chatgroup in chatgroups_followed:
                    if topic not in chatgroup.topic_set.all():
                        chatgroups_counter -= 1
                print(chatgroups_counter)

                if chatgroups_counter == 0:
                    queryset = queryset.exclude(name = topic.name)

        else:
            print("The user is not authenticated, so he will see the entire queryset")
            queryset = Topic.objects.all()


        print(queryset)








        return queryset


class TopicCreate(CreateView):
    model = Topic
    template_name = 'chats/topiccreate.html'
    success_url = '/chatgroups'
    form_class = TopicCreateForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user

        return super(TopicCreate, self).form_valid(form)



class CharGroupFollowToggle(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        chat_group_id = request.POST.get("chat_group_id")
        print(chat_group_id)
        chat_group = ChatGroup.objects.get(id=chat_group_id)
        user =request.user
        if user in chat_group.members.all():
            chat_group.members.remove(user)

        else:
            chat_group.members.add(user)




        return redirect("/chatgroups/")


class ChatGroupCreate(CreateView):
    model = ChatGroup
    template_name = 'chats/chatgroupcreate.html'
    success_url = '/chatgroups'
    form_class = ChatGroupCreateForm



    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user


        return super(ChatGroupCreate, self).form_valid(form)



class ChatGroupList(ListView):
    model = ChatGroup
    template_name = 'chats/chatgrouplist.html'






   # def get_object(self):
    #    chat_group_id = self.kwargs.get("chat_group_id")
     #   if chat_group_id is None:
      #      raise Http404
       # return  get_object_or_404(ChatGroup, id=chat_group_id)







class RecentActivityList(ListView):
    model = Post
    template_name = 'chats/recent_activity_list.html'


'''






class LoginFormView(View):
    form_class = LoginForm
    template_name = 'chats/login.html'


    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):


        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('/register')

        return render(request, self.template_name, {'form': form})





class UserFormView(View):
    form_class = UserForm
    template_name = 'chats/sign_up.html'


    # display blank form

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalised) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)

            user.save()


            # returns User objects if credentials are correct


            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})




def logout_view(request):
    logout(request)
    return redirect('/register')



class NewGroupFormView(View):
    form_class = NewGroupForm
    template_name ='chats/NewChatGroup.html'


    def get(self, request):
        form =self.form_class(None)
        return render(request, self.template_name, {'form': form})


    def post(self, request):


        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            return HttpResponse('It was uploaded')



        else:
            return redirect('/')

        return render(request, self.template_name, {'form': form})







def chatgroup(request, chat_group_id):
    template_name = 'chats/chatgroup.html'
    chat_group = ChatGroup.objects.get(pk=chat_group_id)

    return render(request, template_name, {'chat_group': chat_group})












def chatgroup_follow(request):
    user_id = request.user.id
    chat_group_membership = ChatGroupMembership(request.user.id, 2)


    chat_group_membership.save()


    return HttpResponse('You have successfully followed the chat group')




'''























