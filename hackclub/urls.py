"""hackclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^post/(?P<pk>\d+)/$',	core_views.post_detail,	name='post_detail'),
    url(r'^submit/', core_views.submit, name='submit_post'),
    url(r'^vote/(?P<pk>\d+)/$', core_views.submit_vote, name='submit_vote'),
    url(r'^send_newsreporter/$', core_views.send_newsreporter, name='send_newsreporter'),
    url(r'^search/$', core_views.search_posts, name='search_post'),
    url(r'^(?P<post_id>\d+)/comments/reply/(?P<parent_id>\d+)$', core_views.comment_reply, name='comment_reply'),
]
