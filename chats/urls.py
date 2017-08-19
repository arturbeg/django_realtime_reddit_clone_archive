from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ChatGroupCreate, ChatGroupList, ChatGroupDetailView, CharGroupFollowToggle, TopicCreate, TrendingTopicsList, TrendingLocalChatsList, ProfileDetail
from django.contrib.auth.decorators import login_required






urlpatterns = [

    url(r'^chatgroup/new/$', login_required(ChatGroupCreate.as_view()), name='chatgroup-new'),
    url(r'^chatgroups/$', ChatGroupList.as_view(), name='chatgroups'),
    url(r'^chatgroup/(?P<pk>[-\w]+)/$', ChatGroupDetailView.as_view(), name='chatgroup-detail'),
    url(r'^chatgroup/follow$', CharGroupFollowToggle.as_view(), name='chatgroup-follow'),
    url(r'^topic/new/$', login_required(TopicCreate.as_view()), name='topic-new'),



    url(r'^trending/topics/$', TrendingTopicsList.as_view(), name='trending-topics'),
    url(r'^trending/localchats/$', TrendingLocalChatsList.as_view(), name='trending-localchats'),




    url(r'^u/(?P<pk>[-\w]+)/$', ProfileDetail.as_view(), name='profile'), # user profile





]

'''


urlpatterns = [
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^newgroup/$', views.NewGroupFormView.as_view(), name='newgroup'),
    url(r'^chatgroup/(?P<chat_group_id>[0-9]+)$', views.chatgroup, name='chatgroup'),
   # url(r'^chatgroup/follow/(?P<chat_group_id>[0-9]+)$', views.chatgroup_follow, name='chatgroup_follow'),








] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





'''