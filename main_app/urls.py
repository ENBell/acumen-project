from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
    path('acubox', views.acubox_view),
]
