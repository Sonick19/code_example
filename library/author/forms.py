# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 17:00:18 2023

@author: Sonya
"""
from django import forms

from .models import Author

class AuthorCreateForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic')
