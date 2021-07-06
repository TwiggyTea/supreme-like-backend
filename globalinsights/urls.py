from django.urls import path
from . import views

urlpatterns = [
    path('global-detail', views.globalDetail, name="global-detail"),
    path('global-create', views.globalCreate, name="global-create"),
    path('global-update/<str:pk>/', views.globalUpdate, name="global-update")
]