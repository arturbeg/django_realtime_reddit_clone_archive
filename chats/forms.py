from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, TextInput, PasswordInput, CheckboxInput, FileInput
from .models import ChatGroup, Topic, LocalChat, Profile
from django.core.files.images import get_image_dimensions




#class ProfileCreateForm(forms.ModelForm):
 #   class Meta:
  #      model = Profile
   #     fields = ['user']

class LocalChatCreateForm(forms.ModelForm):
    class Meta:
        model = LocalChat
        fields = ['name', 'about', 'is_hidden', 'is_private', 'avatar']





class ChatGroupCreateForm(forms.ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['avatar','name','about']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Group Name', 'class': 'form-control'}),
            'about': TextInput(attrs={'placeholder': 'About', 'class': 'form-control'}),
        }





class TopicCreateForm(forms.ModelForm):
    class Meta:
        model = Topic

        fields = ['chatgroup', 'name', 'about', 'is_hidden', 'is_private', 'avatar']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Enter Name', 'class': 'form-control'}),
            'about': TextInput(attrs={'placeholder': 'Enter About', 'class': 'form-control'}),
            'is_hidden': CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_private': CheckboxInput(attrs={'class': 'form-check-input'}),
            'avatar': FileInput(attrs={'class': 'form-control-file'}),


        }





class TopicUpdateForm(forms.ModelForm):
    class Meta:
        model = Topic

        fields = ['name', 'about', 'is_hidden', 'is_private', 'avatar']





'''



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        widgets = {
                'email': TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
                'username': TextInput(attrs={'placeholder': 'Username','class': 'form-control'}),



        }


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {

                'username': TextInput(attrs={'placeholder': 'Username','class': 'form-control'}),



        }



'''