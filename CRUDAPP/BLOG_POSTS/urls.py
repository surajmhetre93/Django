from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('post_delete/<int:id>', views.post_delete,  name="POST_DELETE"),
    path('post_form/', views.post_form, name = "POST_FORM"),
    path('post_list/', views.post_list, name="POST_LIST"),
    path('post_update/<int:id>', views.post_update,  name="POST_UPDATE"),
]