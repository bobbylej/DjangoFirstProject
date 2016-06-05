from django import forms            
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm
from polls.models import *    

class RegisterForm(forms.ModelForm):
	password = forms.CharField(max_length=50, widget=forms.PasswordInput)
	repeat_password = forms.CharField(max_length=50, widget=forms.PasswordInput) 
    	class Meta:
        	model = CustomUser
        	fields = ('email','first_name','last_name','gender','phone','city','zip_code','street','no_building','no_local',)
		
		def __init__(self, *args, **kwargs):
			super(RegisterForm, self).__init__(*args, **kwargs)
			self.fields.keyOrder = ['email', 'password', 'repeat_password']
			
class UpdateProfile(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','gender','phone','city','zip_code','street','no_building','no_local',)
		

class ChangePassword(forms.ModelForm):
	old_password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)
	new_password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)
	repeat_new_password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True) 
	
	class Meta:
		model = CustomUser
		fields = ('old_password', 'new_password', 'repeat_new_password')	
