from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^list-image/$',views.list_image, name="list_image"),
    url(r'^upload-image/$',views.upload_image, name="upload_image"),
    url(r'^del-image/$', views.del_image, name="del_image"),
]