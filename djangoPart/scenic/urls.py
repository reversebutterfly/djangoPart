from django.urls import path
from . import views

urlpatterns = [
    path('', views.scenic_list, name='scenic_list'),
    path('heatmap/', views.scenic_heatmap, name='scenic_heatmap'),
    path('spot/<int:spot_id>/', views.scenic_detail, name='scenic_detail'),
]