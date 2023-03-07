# yatube/posts/urls.py (File of urls of the posts app)

from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Home page
    path('', views.index, name='home'),
    # Groups pages
    path('group/<slug:slug>/', views.group_posts, name='group_list')

]
