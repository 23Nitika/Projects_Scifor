from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:poll_id>/', views.detail, name='detail'),
    path('<int:poll_id>/results/', views.results, name='results'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    path('vote_counts/<int:poll_id>/', views.vote_counts, name='vote_counts'),
]