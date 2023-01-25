from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from pictures.forms import PictureForm
from pictures.models import Picture


def index(request):
    """
    Index view to show all images and provide upload form.
    """
    pictures = Picture.objects.all()
    return render(request, 'pictures/index.html', {'pictures': pictures})


class IndexView(generic.ListView):
    model = Picture
    template_name = 'pictures\index.html'


def upload(request):
    """
    View to handle image upload.
    """
    image = request.FILES.get('image')
    title = request.POST['title']
    new_img = Picture(title=title, image=image)
    new_img.save()
    return redirect(reverse('pictures:function'))


class CreatePictureView(generic.CreateView):
    """
    CreateView for `Picture` objects.
    """
    model = Picture
    form_class = PictureForm
    template_name = 'pictures\picture_create.html'

    ####################################################################
    # Which of these is better?
    success_url = reverse_lazy('pictures:class')

    # def get_success_url(self):
    #     return reverse('pictures:index')
    ####################################################################