from . import views
from django.urls import path

urlpatterns = [path('count/', views.homepage, name='home'),
               path('delete/', views.delete_count, name='delete_cookie')
    ]