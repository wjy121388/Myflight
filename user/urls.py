
from django.conf.urls import url,include
from django.contrib import admin
# from .views import ForCodeView
from user import  views
urlpatterns = [

    url(r'^login/', views.login),
    url(r'^getVerifiedCodeapi/', views.getVerifiedCodeapi),
    # url('forcode/',ForCodeView.as_view(),name='forcode'),
]