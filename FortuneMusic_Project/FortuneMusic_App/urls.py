from django.urls import path
from . import views

app_name = 'FortuneMusic_App'
urlpatterns = [
    path(r'', views.index, name='index'),
    # 以下を追記(views.pyのcall_write_data()にデータを送信できるようにする)
    path("ajax/", views.call_file, name="call_file"),
]