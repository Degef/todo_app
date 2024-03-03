from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('add_todo/', views.add_todo, name='add_todo'),
	path('delete/<int:pk>/', views.delete, name='delete'),
	path('update/<int:pk>/', views.update, name='update'),
]