from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', blog_home, name='blog_home'),
    url(r'^posts/$', post_list, name='post_list'),
    url(r'^post/(\d+)', post_detail, name='post_detail'),
    url(r'^posts/create', create_post, name='create_post'),
    url(r'^edit_post/(\d+)', edit_post, name='edit_post'),
    url(r'delete/(\d+)', delete_post, name='delete_post'),
    
   
]