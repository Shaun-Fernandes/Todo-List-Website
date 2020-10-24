from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:folder_id>/', views.folder, name='folder'),
    path('entry/new/', views.EntryCreateView.as_view(), name='new_entry'), 
    path('entry/<int:entry_id>/', views.update_entry, name='update_entry'),
]
