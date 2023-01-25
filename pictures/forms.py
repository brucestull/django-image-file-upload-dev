from django import forms

from pictures.models import Picture


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = (
            'title',
            'image',
        )