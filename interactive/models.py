from django.db import models
from chats.models import ChatGroup, LocalChat, Topic, GlobalChat
from django.conf import settings


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


    def __str__(self):
        return str(self.user.username) + "  " + self.text[:20]

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')

    def as_dict(self):
        return {'user': self.user.username, 'text': self.text, 'timestamp': self.formatted_timestamp}
