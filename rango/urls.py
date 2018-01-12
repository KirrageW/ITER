from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.about, name='about'),
    url(r'^about/', views.about, name='about'),
    ]
