from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add', views.add, name="add"),
    path('test',views.test,name="test"),
    # path('wel/', views.ReactView.as_view(), name="something"),
]