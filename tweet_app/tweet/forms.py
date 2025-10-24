from django import forms
from .models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'photo']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full p-3 rounded-lg bg-gray-700 border border-gray-600 focus:ring-2 focus:ring-yellow-400 focus:outline-none text-white',
                'rows': 4,
                'placeholder': 'What’s happening?',
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'p-2 block w-full text-sm text-gray-300 bg-gray-700 border border-gray-600 rounded-lg cursor-pointer focus:ring-yellow-400 focus:border-yellow-400',
            }),
        }
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    image = forms.ImageField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'image')
