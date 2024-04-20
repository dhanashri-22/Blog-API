from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get-all-posts/',views.GetAllPosts),
    path('create-new-post/',views.CreatePost),
    path('delete_post/',views.DeletePost),
    path('get_post/',views.Getpost),
    path('update_post/',views.UpdatePost),
]
