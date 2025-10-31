from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('l3info', views.index, name='home'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('our-services.html', views.services,name='services')
    ,path('services-detail.html', views.services_detail, name='services_detail')
    ,path('gallery.html', views.gallery, name='gallery')
    ,path('team.html', views.team, name='team')
    ,path('pricing.html', views.pricing, name='pricing')
    ,path('blog.html', views.blog, name='blog')
    ,path('single-blog-post-right-sidebar.html', views.single_blog_right, name='single_blog_right')
    ,path('single-blog-post-left-sidebar.html', views.single_blog_left, name='single_blog_left')
    ,path('single-blog-post-without-sidebar.html', views.single_blog_no_sidebar, name='single_blog_no_sidebar')
]