from django.urls import path
from .views import HomeView
urlpatterns = [
    #path('home/', HomeView.as_view(), name = 'blog-home')
    path('', HomeView.as_view(), name = 'blog-home')
]
