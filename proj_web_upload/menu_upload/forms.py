# Di dalam file forms.py di dalam aplikasi menu_upload

from django import forms # type: ignore
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['owner_name', 'image']