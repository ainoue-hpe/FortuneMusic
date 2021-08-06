from django.urls import path
from . import views

app_name='Test_App'
urlpatterns = [
    path(r'',views.index,name='index'),

    path("ajax/", views.call_write_data, name="call_write_data"),
]
