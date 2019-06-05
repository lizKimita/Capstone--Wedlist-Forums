from .models import Status,Profile,Posts, Solutions
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['profile','pub_date', 'poster_id']


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'userId']

class NewSolutionsForm(forms.ModelForm):
    class Meta:
        model = Solutions
        exclude = ['post_id', 'user']