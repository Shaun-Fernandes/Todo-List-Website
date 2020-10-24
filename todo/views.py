from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden, Http404
from .models import Folder, Entry
from .forms import EntryCreationForm


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

@login_required
def new_entry(request):
    if request.method == 'POST':
        form = EntryCreationForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your new To Do entry has been saved")
            return redirect('todo:folder', folder_id = form.cleaned_data['folder'].id)
    else:
        form = EntryCreationForm(request.user)

    return render(request, "todo/entry_form.html", {'form' : form})


@login_required
def update_entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    if request.user != entry.folder.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = EntryCreationForm(request.user, request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your To Do entry has been updated!")
            return redirect('todo:folder', folder_id = form.cleaned_data['folder'].id)
    else:
        form = EntryCreationForm(request.user, instance=entry)

    return render(request, "todo/entry_form.html", {'form' : form, 'entry_id':entry_id})


class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Entry
    success_url = "/"

    def test_func(self):
        entry = self.get_object()
        if self.request.user == entry.folder.user:
            return True
        return False


class FolderCreateView(LoginRequiredMixin, CreateView):
    model = Folder
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FolderCreateView, self).form_valid(form)


class FolderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Folder
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FolderUpdateView, self).form_valid(form)

    def test_func(self):
        folder = self.get_object()
        if self.request.user == folder.user:
            return True
        return False


class FolderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Folder
    success_url = "/"

    def test_func(self):
        folder = self.get_object()
        if self.request.user == folder.user:
            return True
        return False
