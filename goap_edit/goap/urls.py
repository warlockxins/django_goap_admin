from django.urls import path

from . import views

urlpatterns = [
    path('<id>', views.index, name='index'),
    path('<id>/playground', views.playground, name='playground')
]
