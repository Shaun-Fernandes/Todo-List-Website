from django import forms
from .models import Folder, Entry


class EntryCreationForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['name', 'description', 'due_date', 'priority', 'folder', 'completed']

    def __init__(self, user, *args, **kwargs):
        super(EntryCreationForm, self).__init__(*args, **kwargs)
        self.fields['folder'].queryset = user.folder_set
