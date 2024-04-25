from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('about/', views.about_view, name='about'),
    path('members/',views.members, name='members'),
    path('experience/',views.experience_view, name='experience'),
    path('projects/', views.projects_view, name='projects'),
    path('contact/', views.contact_view, name='contact'),
]
