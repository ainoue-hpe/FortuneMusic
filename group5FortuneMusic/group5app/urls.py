from django.urls import path
from . import views

app_name = 'group5app'
urlpatterns = [
    path(r'', views.index, name='index'),
]

#新規作成