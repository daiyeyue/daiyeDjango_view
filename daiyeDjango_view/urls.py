"""daiyeDjango_view URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from teacher_app import views as v

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^teacher_app/', v.teacher ),
    url(r'^v2_exp/', v.v2_exception ),

    url(r'^v10_1/',v.v10_1),
    url(r'^v10_2/',v.v10_2),
    url(r'^v11/',v.v11_1, name='v11'),
    url(r'^v8/',v.v8_get),
    url(r'^v9_get/',v.v9_get),
    url(r'^v9_post/',v.v9_post),
    url(r'^render_test/',v.render_test),
    url(r'^render2_test/',v.render2_test),
    url(r'^render3_test/',v.render3_test),
    url(r'^render1_to_response/',v.render4_test),
    url(r'^get404/',v.get404),

]
