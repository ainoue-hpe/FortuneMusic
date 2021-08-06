from django.urls import path
from . import views

app_name = 'group5app'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'sub', views.sub, name='sub'),
]

#新規作成