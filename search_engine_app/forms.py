from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# The below is the radio buttons options for the sentiments
sentimentOptions = [
                        ('positive', 'Positive'),
                        ('negative', 'Negative'),
                        ('na', 'Neutral'),
                   ]

"""
This GeneralForms class is used for storing all the vital search information in the form such as the user's search query and the sentiment options
    @Parameters:
        forms.Forms: This is a default form provided by Django
    File Reference: home.html
"""    
class GeneralForms(forms.Form):
    name = forms.CharField(label = '', widget=forms.TextInput(attrs={'placeholder':'  Search....'}))
    options = forms.CharField(label='Please select the sentiment', widget=forms.RadioSelect(choices=sentimentOptions))


"""
This userPortalForms class is used for storing all the information such as the topic and the sentiment that the user would like to save in their portal
    @Parameters:
        forms.Forms: This is a default form provided by Django
    File Reference: userPortal.html
"""  
class userPortalForms(forms.Form):
    topic = forms.CharField(label = '', widget=forms.TextInput(attrs={'placeholder':'  Enter topic to follow up'}))
    options =forms.CharField(label="", widget=forms.Select(choices=sentimentOptions))


"""
This feedBackForm class is used for storing all the information such as the subject, email and the message that the user would like to give the feedback
    @Parameters:
        forms.Forms: This is a default form provided by Django
    File Reference: feedBack.html
"""
class feedBackForm(forms.Form):
    subject = forms.CharField(label = 'Subject', widget = forms.TextInput(attrs = {'placeholder': ' Enter the subject'}))
    email = forms.CharField(label = 'Enter your e-mail address', widget = forms.TextInput(attrs = {'placeholder': ' Enter your E-mail address'}))
    message = forms.CharField(label = 'Enter your message', widget=forms.Textarea(attrs = {'placeholder': ' Enter your message'}))


"""
This loginForm class is used for storing all the information such as the user name and the password to login to their portal
    @Parameters:
        forms.Forms: This is a default form provided by Django
    File Reference: login.html
"""
class loginForm(forms.Form):
    uname = forms.CharField(label = 'Username', widget=forms.TextInput(attrs={'placeholder':' Username'}))
    pwd = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'placeholder':' Password'}))


"""
This signUpForm class is used for storing all the information of a new user such as the name, email, password to register as a new user
    @Parameters:
        forms.Forms: This is a default form provided by Django
    File Reference: register.html
"""
class signUpForm(forms.Form):
    newName = forms.CharField(label = 'Enter you name', widget=forms.TextInput(attrs={'placeholder':' Enter your name'}))
    email = forms.CharField(label = 'Enter your e-mail address', widget = forms.TextInput(attrs = {'placeholder': ' Enter your E-mail address'}))
    pwd = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'placeholder':' Enter a new password'}))
    pwdr = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'placeholder':' Re-enter the password'}))

"""
This CreateUserForm class is used for storing all the information of a new user such as the name, email, password to register as a new user.
The form details would be directly stored in the database, thanks to Django Model forms
    @Parameters:
        User CreationForm: This is a default user registration form provided by Django
    File Reference: register.html
"""
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
