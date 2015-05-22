from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from contacts import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'all_contacts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello_you/([A-Za-z]+)/$', views.hello_you),
    url(r'^contact_list/', views.contact_list),
    url(r'^contact_form/', views.contact_form),
    url(r'^edit_contact/(\d+)/$', views.edit_contact),
    url(r'^delete_contact/(\d+)/$', views.delete_contact),
)
