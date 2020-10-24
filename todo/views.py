from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Folder, Entry


@login_required
def home(request):
    context = {
        "folders": request.user.folder_set.all(),
    }
    return render(request, "todo/home.html", context)

@login_required
def folder(request, folder_id):
    try:
        folder = Folder.objects.get(pk=folder_id)
        if folder.user != request.user:
            return home(request)
    except Folder.DoesNotExist:
        return home(request)

    context = {
        "folders": request.user.folder_set.all(),
        "current_folder": folder
    }
    return render(request, "todo/home.html", context)


# @login_required
# def new_entry(request):
#     return HttpResponse(f"You creating new entry")


class EntryCreateView(CreateView):
    model = Entry
    fields = ['name', 'description', 'due_date', 'priority']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookCreate, self).form_valid(form)


@login_required
def update_entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    if entry.folder.user != request.user:
        raise Http404("No Entry matches the given query.")
    return HttpResponse(f"You're looking at entry {entry_id} <br> <h1> {entry.name} </h1>, {entry.description}, {entry.due_date}, {entry.priority}, {entry.completed}")
