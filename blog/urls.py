from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', blog_home, name='blog_home'),
    url(r'^view_blog', view_blog, name='view_blog'),
   
]