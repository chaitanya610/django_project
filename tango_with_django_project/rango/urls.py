from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'^about/$', views.about, name = 'about'),
    re_path(r'^add_category/$', views.add_category, name = 'add_category'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name = 'show_category'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name = 'add_page'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'^logout/$', views.user_logout, name='logout'),
    re_path(r'^search/$', views.search, name='search'),
    re_path(r'^goto/$', views.track_url, name='goto'),
    re_path(r'^like_category/$', views.like_category, name='like_category'),
    re_path(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
    re_path(r'^auto_add_page/$', views.auto_add_page, name='auto_add_page')
]

