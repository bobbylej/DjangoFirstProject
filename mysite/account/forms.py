from django import forms            
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm
from polls.models import *
from account.models import * 

class RegisterForm(forms.ModelForm):
	password1 = forms.CharField(max_length=32, widget=forms.PasswordInput) 
    	class Meta:
        	model = CustomUser
        	fields = ('email','first_name','last_name','groups','gender','phone','city','zip_code','street','no_building','no_local',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Muscle
        # exclude = ['author', 'updated', 'created', ]
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say something...'}
            ),
        }

