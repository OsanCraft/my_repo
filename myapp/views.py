from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def gallery(request):
    images = UploadedImage.objects.all()
    return render(request, 'gallery.html', {'images': images})

def home(request):
    return render(request, 'home.html')
