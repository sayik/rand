from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # this function post_detail itself is passed so that post/<int:pk> is passed
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('kappa/<str:who>/', views.who_made, name='who'),
]
