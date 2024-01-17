from django import forms
from . import models

class BookDonateForm(forms.ModelForm):
    class Meta:
        model = models.BookDonateModel
        # fields = '__all__'
        exclude = ['user']