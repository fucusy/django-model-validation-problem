from django.conf.urls import patterns, include, url
from django.contrib import admin
from validation import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'model_validation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^validate/', views.validation),
    url(r'^admin/', include(admin.site.urls)),
)
