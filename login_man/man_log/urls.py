from django.conf.urls import url
from . import views

app_name = 'man_log'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    # url(r'^login/', views.login_man),
    # url(r'^logout', views.logout),
    # url(r'^login', views.index),
]