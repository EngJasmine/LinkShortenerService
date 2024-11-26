from django.urls import path
from .views import index,root_link,add_link

urlpatterns = [
    path('', index, name='home'),
    path('<str:slug_link>/', root_link, name='root-link'),
    path('link/create', add_link, name='create-link'),
]