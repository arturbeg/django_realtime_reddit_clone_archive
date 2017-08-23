from django.db import models
#from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from datetime import datetime
from django.urls import reverse



User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User)
    followers = models.ManyToManyField(User, blank=True, related_name="is_following")
    about = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to="profile_avatar", blank=True)


  #  following = models.ManyToManyField(User, related_name="following")
    timestamp = models.DateTimeField(auto_now_add=True)



    def get_number_of_followers(self):
        return self.followers.count()

    def get_number_of_following(self):
        return self.user.is_following.count()


    def __str__(self):
        return self.user.username



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
    label = models.SlugField(unique=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chatgroup', kwargs={'pk': self.pk})








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


    def __str__(self):
        return self.name









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

    def __str__(self):
        return self.name



class GlobalChat(models.Model):
    chatgroup = models.OneToOneField(ChatGroup, on_delete=models.CASCADE) # the parent chat group -> one to one relationship
    #label = models.SlugField(unique=True)


    def __str__(self):
        return self.chatgroup.name



def post_save_user_receiver(sender, instance, created, *args, **kwargs): # check if it is working/more research on signals
    if created:
        globalchat, is_created = GlobalChat.objects.get_or_create(chatgroup=instance)

post_save.connect(post_save_user_receiver, sender=ChatGroup)


'''



class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User)
    chatgroup = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    globalchat = models.ForeignKey(GlobalChat, on_delete=models.CASCADE, blank=True, null=True)
    localchat = models.ForeignKey(LocalChat, on_delete=models.CASCADE, blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


'''

#class ChatGroupMembership(models.Model):
 #   user = models.ForeignKey(User, on_delete=models.CASCADE)
  #  chat_group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
   # date_established = models.DateTimeField(default=datetime.now, blank=True)



#class LocalChatMembership(models.Model):
 #   user = models.ForeignKey(User, on_delete=models.CASCADE)
  #  local_chat = models.ForeignKey(LocalChat, on_delete=models.CASCADE)
   # date_joined = models.DateTimeField()




    # class ChatGroupMembership(models.Model):
    #   user = models.ForeignKey(User, on_delete=models.CASCADE)
    #  chat_group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    # date_established = models.DateTimeField(default=datetime.now, blank=True)



