from . import views
from django.urls import path

urlpatterns = [path('', views.index),
               path('cats/',views.post_proc),
               path('<int:pk>', views.CatsDetailView.as_view(), name='mydetail'),
               path('cat/', views.CatsListView.as_view()),
               path('my/', views.MyDetailView.as_view())
               ]
