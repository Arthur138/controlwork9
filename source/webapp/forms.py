from django import forms
from webapp.models import Ads , Comment

class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ["title", "description", "category", "picture", "price"]



class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
