from django.views import generic
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from .models import Album
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q



class IndexView(generic.ListView):

    template_name = 'music/home.html'


    def get_queryset(self):
        return quit()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'






class AlbumCreate(CreateView):
    model = Album

    fields = ['artist','album_title' ,'genr' ,'album_logo', ]


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genr','album_logo']




class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')



