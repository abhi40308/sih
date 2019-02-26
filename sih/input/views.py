from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView, DetailView
from .models import InputImage
from .forms import InputImageForm

class InputImageView(FormView):
    template_name = 'image_upload.html'
    form_class = InputImageForm

    def form_valid(self, form):
        input_image = InputImage(
            image=self.get_form_kwargs().get('files')['image'])
        input_image.save()
        self.id = input_image.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('input_image', kwargs={'pk': self.id})

class InputDetailView(DetailView):
    model = InputImage
    template_name = 'image_detail.html'
    context_object_name = 'image'