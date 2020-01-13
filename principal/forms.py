# -*- encoding: utf-8 -*-
from django import forms

class UserForm(forms.Form):
    id = forms.CharField(label='User ID')
    
class AnimeForm(forms.Form):
    id = forms.CharField(label='Anime ID')