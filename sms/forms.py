from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Outgoing,Category, Upload




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserRegisterForm1(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class SendForm(forms.Form):

    class Meta:
        model = Outgoing
        fields = ["phone_numbers", "text_message"]

class CategoryForm(forms.Form):
    class Meta:
        model = Category
        fields = ('name',)

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ["csv"]
