from django.urls import path, include
from myapp import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.about),
    path('contact/', views.contact),
    path('register/', views.form_view, name="register"),
    path('success/', views.success, name='success'),
    
]