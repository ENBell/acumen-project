from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
    path('acubox/<site_id>/',views.acubox_view),

]
