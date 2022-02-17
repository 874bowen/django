from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.sessfun),
    path('email/',views.email, name='email'),
    ]