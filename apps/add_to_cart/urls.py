from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^show_cart$', views.show_cart),
    url(r'^clear_cart$', views.clear_cart)
]
