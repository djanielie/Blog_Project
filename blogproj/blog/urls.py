from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('next', views.casual_page, name='casual-page'),
]
