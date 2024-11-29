from . import views
from django.urls import path

urlpatterns = [
    # Corrected the path for the home page
    path('', views.PostList.as_view(), name='home'),  # This should handle the root URL '/'
    
    # This path is for individual blog posts by their slug
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]