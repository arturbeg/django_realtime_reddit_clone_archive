from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from datetime import datetime
from django.urls import reverse
import interactive



User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User)
    followers = models.ManyToManyField(User, blank=True, related_name="is_following")
    about = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to="profile_avatar", blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)



    def get_number_of_followers(self):
        return self.followers.count()

    def get_number_of_following(self):
        return self.user.is_following.count()


    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    def get_absolute_url_for_avatar(self):
        print(self.avatar is None)
        if not self.avatar:
            print("This user has not provided an avatar")
            return reverse("media", kwargs={'path': "profile_avatar/default-avatar.png"})

        else:
            return  reverse("media", kwargs={'path': self.avatar})



    def get_absolute_url_followers(self):

        return reverse("profile-followers", kwargs={'pk': self.pk})


    def get_absolute_url_following(self):
        return reverse("profile-following", kwargs={'pk': self.pk})

    def get_absolute_url_chatgroups(self):

        return reverse("profile-chatgroups", kwargs={'pk': self.pk})






def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=User)



class ChatGroup(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    members = models.ManyToManyField(User, related_name="is_member")
    timestamp = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to="group_avatar", blank=True)


    def get_absolute_url_for_avatar(self):
        return reverse("media", kwargs={'path': self.avatar})



    def get_owner(self):
        return self.owner


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chatgroup-detail', kwargs={'pk': self.pk})








class Topic(models.Model):
    chatgroup = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)  # the parent chat group
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User)
    about = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    arrow_ups = models.IntegerField(default=0)
    arrow_downs = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to="topic_avatar", blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    label = models.SlugField(unique=True)

    def get_name(self):
        return self.name


    def get_owner(self):
        return self.owner.id


    def get_chatgroup_owner(self):
        return self.chatgroup.owner


    def __str__(self):
        return self.name


    def get_room_type(self):
        return "Topic"

    def get_absolute_url(self):
        return reverse('chatroom', kwargs={'chat_room_type': 'topic', "label": self.label})


    def get_the_most_recent_message(self):

        list_of_messages = self.topic_messages.order_by('-timestamp')[:1]

        if len(list_of_messages) == 0:
            print("There is no messages in the local chat")
            top_message = interactive.models.Message.objects.get(pk=180)


        else:
            top_message = list_of_messages[0]
            print(top_message.text)

        return top_message

    def get_absolute_url_for_avatar(self):
        return reverse("media", kwargs={'path': self.avatar})









class LocalChat(models.Model):
    chatgroup = models.ForeignKey(ChatGroup, on_delete=models.CASCADE) # the parent chat group
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="local_chat_avatar", blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(User, related_name="is_participant")
    label = models.SlugField(unique=True)


    def get_name(self):
        return self.name

    def get_owner(self):
        return self.chatgroup.owner.id

    def get_room_type(self):
        return "Local Chat"

    def get_absolute_url_for_avatar(self):
        return reverse("media", kwargs={'path': self.avatar})

    def get_absolute_url(self):
        return reverse('chatroom', kwargs={'chat_room_type': 'localchat', "label": self.label})


    def get_number_of_participants(self):
        return self.participants.count()


    def get_the_most_recent_message(self):

        list_of_messages = self.localchat_messages.order_by('-timestamp')[:1]

        if len(list_of_messages) == 0:
            print("There is no messages in the local chat")
            top_message = interactive.models.Message.objects.get(pk=180)


        else:
            top_message = list_of_messages[0]
            print(top_message.text)

        return top_message


    def __str__(self):
        return self.name



class GlobalChat(models.Model):
    chatgroup = models.OneToOneField(ChatGroup, on_delete=models.CASCADE) # the parent chat group -> one to one relationship
    label = models.SlugField(unique=True)

    def get_name(self):
        return self.chatgroup.name

    def get_owner(self):
        return self.chatgroup.owner.id

    def get_room_type(self):
        return "Global Chat"

    def get_absolute_url_for_avatar(self):
        return reverse("media", kwargs={'path': self.chatgroup.avatar}) # Uses the same avatar as the chatgroup it belongs to


    def __str__(self):
        return self.chatgroup.name


    def get_globalchat_name(self):
        return self.chatgroup.name

    def get_absolute_url(self):
        return reverse('chatroom', kwargs={'chat_room_type': 'globalchat', "label": self.label})

    def get_the_most_recent_message(self):

        list_of_messages = self.globalchat_messages.order_by('-timestamp')[:1]

        if len(list_of_messages) == 0:
            print("There is no messages in the local chat")
            top_message = interactive.models.Message.objects.get(pk=180)


        else:
            top_message = list_of_messages[0]
            print(top_message.text)

        return top_message



def post_save_chatgroup_receiver(sender, instance, created, *args, **kwargs): # check if it is working/more research on signals
    if created:
        globalchat, is_created = GlobalChat.objects.get_or_create(chatgroup=instance, label=instance.name)

post_save.connect(post_save_chatgroup_receiver, sender=ChatGroup)

