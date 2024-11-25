from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm
from . import forms
from . import models


class MusicianListView(ListView):
    model = Musician
    template_name = 'home.html'
    context_object_name = 'musicians'


@method_decorator(login_required, name='dispatch')
class MusicianCreateView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('musician_list')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class MusicianUpdateView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class AlbumCreateView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_Post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class AlbumUpdateView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class AlbumDeleteView(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'
