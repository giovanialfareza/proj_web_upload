# Di dalam file views.py di dalam aplikasi menu_upload

from django.shortcuts import render, redirect # type: ignore
from .forms import PhotoForm

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success') # Redirect ke halaman sukses upload
    else:
        form = PhotoForm()
    return render(request, 'menu_upload/upload_photo.html', {'form': form})
    
def upload_success(request):
    return render(request, 'menu_upload/upload_success.html')

from .models import Photo
def photo_list(request):
    photos = Photo.objects.all()
    context = {'photos' : photos}
    return render(request, 'menu_upload/photo_list.html', context)