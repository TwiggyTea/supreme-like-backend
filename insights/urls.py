from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('insight-list', views.insightList, name="insight-list"),
    path('insight-detail/<str:pk>/', views.insightDetail, name="insight-detail"),
    path('insight-create', views.insightCreate, name="insight-create"),
    path('insight-update/<str:pk>/', views.insightUpdate, name="insight-update"),
    path('insight-delete/<str:pk>/', views.insightDelete, name="insight-delete"),
]