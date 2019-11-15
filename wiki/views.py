from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from wiki.models import Page
from wiki.forms import PageForm
from django.http import HttpResponseRedirect
from django.urls import reverse


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })


class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })


class CreatePageForm(FormView):
    """Renders a form for user to create a new form."""
    template_name = 'add_page.html'
    form = PageForm
    success_url = 'create'

    def get(self, request):
        """Renders the form on a HTTP GET request."""
        form = PageForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
'''
def get_page(request):
    if request.method == 'POST':
        form = PageForm()
        if form.is_valid():
            form = PageForm(request.POST or None)
            new_page = form.save(commit=False)
            new_page.author = user.username
            new_page.save()
            return HttpResponseRedirect(reverse('wiki-details-view',
                                                args=(new_page.slug,)))
    else:
        form = PageForm()
        return render(request, 'add_page.html', {'form': form})
'''
