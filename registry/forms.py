from django import forms

from .models import Passport


class PassportAdminForm(forms.ModelForm):

    class Meta:
        model = Passport
        exclude = ('id', )
