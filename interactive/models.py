from django.db import models
from chats.models import ChatGroup, LocalChat, Topic, GlobalChat
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import post_save


User = settings.AUTH_USER_MODEL

# You are in the django_channels branch

class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User)
    chatgroup = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, blank=True, null=True, related_name="chatgroup_messages")
    globalchat = models.ForeignKey(GlobalChat, on_delete=models.CASCADE, blank=True, null=True, related_name="globalchat_messages")
    localchat = models.ForeignKey(LocalChat, on_delete=models.CASCADE, blank=True, null=True, related_name="localchat_messages")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True, related_name="topic_messages")
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    # new fieds
    likers = models.ManyToManyField(User, blank=True, related_name="likers")
    dislikers = models.ManyToManyField(User, blank=True, related_name="dislikers")



    def __str__(self):
        return str(self.user.username) + " : " + self.text[:40]

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')

    def get_absolute_url_room(self): # get the absolute url of the room the message is in
        if self.globalchat:
            return reverse("chatroom", kwargs={'chat_room_type': "globalchat", 'label': self.globalchat.label })
        elif self.topic:
            return reverse("chatroom", kwargs={'chat_room_type': "topic", 'label': self.topic.label})

        elif self.localchat:
            return reverse("chatroom", kwargs={'chat_room_type': "localchat", 'label': self.localchat.label})




    def get_number_of_likes(self):
        return self.likers.count()

    def get_number_of_dislikes(self):
        return self.dislikers.count()


    def has_related_post(self):
        return hasattr(self, 'post')

    def get_url_for_avatar_of_message_sender(self):
        return reverse("media", kwargs={'path': self.user.profile.avatar})

    def as_dict(self):
        return {'user': self.user.username, 'text': self.text, 'timestamp': self.formatted_timestamp, 'profile_avatar': self.get_url_for_avatar_of_message_sender()}





class Post(models.Model):
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.message.text[:40]

    def get_number_of_comments(self):
        return self.postcomment_set.all().count()





class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    likers = models.ManyToManyField(User, blank=True, related_name="comment_likers")
    dislikers = models.ManyToManyField(User, blank=True, related_name="comment_dislikers")


    def __str__(self):
        return self.text[:40]
