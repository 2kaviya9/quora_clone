from django import forms
from .models import QuoraPost, QuoraReply
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class QuoraPostForm(forms.ModelForm):
    class Meta:
        model = QuoraPost
        fields = ['question', 'image']

class QuoraReplyForm(forms.ModelForm):
    class Meta:
        model = QuoraReply
        fields = ['answer', 'image']
        widgets = {
            'answer': forms.Textarea(attrs={'class': 'reply-textarea'}),
            'image': forms.ClearableFileInput(attrs={'class': 'reply-image'}),
        }
