from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (FormView, CreateView, ModelFormMixin,
                                       UpdateView)
from wiki.models import Page
from wiki.forms import PageForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.template import loader


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page
    template_name = 'wiki/list.html'

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, self.template_name, {
          'pages': pages
        })


class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page
    template_name = 'wiki/page.html'

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, self.template_name, {
          'page': page
        })


class PageCreate(CreateView):
    '''Render a form to create a new page.'''
    model = Page
    fields = ["title", "content"]
    object = None  # new Page to be created
    template_name = 'wiki/add_page.html'

    def form_valid(self, form, request):
        """Creates the new Page, and makes the user who submitted
           the form the author.
        """
        self.object = form.save(commit=False)
        user = User.objects.get(username=request.user)
        self.object.author = user
        self.object = form.save()
        return super(ModelFormMixin, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        """Override the CreateView post method, so that it invokes
           the subclass form_valid, which includes a parameter for request.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)


class PageUpdate(UpdateView):
    '''Render a form to update a page.'''
    model = Page
    fields = ['title', 'content']
    template_name_suffix = "_edit_form"
