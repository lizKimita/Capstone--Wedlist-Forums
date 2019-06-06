from .models import Status,Profile,Posts, Solutions,Tips
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
    
class NewTipsForm(forms.ModelForm):
    class Meta:
        model = Tips
        exclude = ['user', 'date', 'tipper_id', 'upvote', 'downvote']

class NewvotesForm(forms.ModelForm):
    class Meta:
        model = Tips
        exclude = ['upvote', 'downvote', 'user', 'title', 'tipper_id', 'tips','date']

class NewdownvoteForm(forms.ModelForm):
    class Meta:
        model = Tips
        exclude = ['upvote', 'downvote', 'user', 'title', 'tipper_id', 'tips','date']