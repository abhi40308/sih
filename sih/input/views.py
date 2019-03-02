import os
from django.core.files.base import File
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView, DetailView
from .models import InputImage
from .forms import InputImageForm
import gzip
import shutil

class InputImageView(FormView):
    template_name = 'image_upload.html'
    form_class = InputImageForm

    def form_valid(self, form):
        input_image = InputImage(
            image=self.get_form_kwargs().get('files')['image'])
        input_image.save()
        self.id = input_image.id

        s = input_image.image.path
        s = s[0:-3]

        if(input_image.extension() == ".gz"):
            with gzip.open(input_image.image.path,'rb') as f_in:
                with open(s,'wb') as f_out:
                    shutil.copyfileobj(f_in,f_out)

        s = s[58:]

        input_image = InputImage( image = s)
        input_image.save()
        self.id = input_image.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('input_image', kwargs={'pk': self.id})

class InputDetailView(DetailView):
    model = InputImage
    template_name = 'image_detail.html'
    context_object_name = 'image'

class OutputView(DetailView):
    model = InputImage
    template_name = 'image_output.html'
    context_object_name = 'image'