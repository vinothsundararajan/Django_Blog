from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Entry
# Create your views here.

class HomeView(ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = "blog_entries"
    ordering = ['-entry_date']
    paginate_by = 3

class EntryView(DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html'

class CreateEntryView(CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = [ 'entry_title', 'entry_text' ]

    def form_valid(self,form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)

def contact(request):
    template_name = 'entries/contact.html'
    return render(request, 'entries/contact.html',{})