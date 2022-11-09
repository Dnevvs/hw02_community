from django.urls import path
from posts import views


app_name = 'group_list'

urlpatterns = [
    path('', views.index, name='home'),
    path('group/<slug:slug>', views.group_posts, name='group_list')
]
