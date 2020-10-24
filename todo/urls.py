from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:folder_id>/', views.folder, name='folder'),
    path('entry/new/', views.new_entry, name='new_entry'),
    path('entry/<int:entry_id>/', views.update_entry, name='update_entry'),
    path('entry/<int:pk>/delete/', views.EntryDeleteView.as_view(), name='delete_entry'),

    path('new/', views.FolderCreateView.as_view(), name='create_folder'),
    path('<int:pk>/update/', views.FolderUpdateView.as_view(), name='update_folder'),
    path('<int:pk>/delete/', views.FolderDeleteView.as_view(), name='delete_folder'),
]
