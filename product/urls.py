from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'product'

urlpatterns = [
    # products
    url(r'^$', views.indexview, name="index"),

    # products/detail/product_id/
    url(r'detail/(?P<product_id>[0-9]+)/$', views.detailview, name="detail"),

    # product/result/product_id/
    url(r'result/(?P<product_id>[0-9]+)/$', views.resultview, name="result"),

    # product/votes/product_id/
    url(r'votes/(?P<product_id>[0-9]+)/$', views.votesview, name="votes"),
]