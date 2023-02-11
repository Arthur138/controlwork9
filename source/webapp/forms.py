from django import forms
from webapp.models import Ads

class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ["title", "description", "category", "picture", "price", "status"]