from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', blog_home, name='blog_home'),
    url(r'^post_list', post_list, name='post_list'),
    url(r'^post_detail/(\d+)', post_detail, name='post_detail'),
    url(r'^new_post', new_post, name='new_post'),
    url(r'^edit_post/(\d+)', edit_post, name='edit_post'),
    
   
]