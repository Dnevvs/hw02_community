from django.contrib import admin
from django.urls import include, path
from posts import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]
