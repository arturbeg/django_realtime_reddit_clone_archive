from django.db import models
from chats.models import ChatGroup, LocalChat, Topic, GlobalChat
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User)
    chatgroup = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    globalchat = models.ForeignKey(GlobalChat, on_delete=models.CASCADE, blank=True, null=True)
    localchat = models.ForeignKey(LocalChat, on_delete=models.CASCADE, blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

