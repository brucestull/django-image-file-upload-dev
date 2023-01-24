from django.shortcuts import render, redirect
from django.urls import reverse

from pictures.models import Image


def index(request):
    """
    Index view to show all images and provide upload form.
    """
    images = Image.objects.all()
    return render(request, 'pictures/index.html', {'images': images})


def upload(request):
    """
    View to handle image upload.
    """
    img = request.FILES.get('picture')
    title = request.POST['title']
    new_img = Image(title=title, img=img)
    new_img.save()
    return redirect(reverse('pictures:index'))
