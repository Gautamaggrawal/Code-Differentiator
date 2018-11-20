from django.conf.urls import url,include
from . import views

app_name='cpd'
urlpatterns = [
    url('^$',views.home,name="home"),
    ]


    