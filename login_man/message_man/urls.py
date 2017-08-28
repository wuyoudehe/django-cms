from django.conf.urls import url
from . import views

app_name = 'message_man'
urlpatterns = [
	url(r'^add/', views.message_ajax),
	url(r'^weidu/', views.message_num),
]