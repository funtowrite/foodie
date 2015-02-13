from django.conf.urls import patterns, include, url
from django.contrib import admin

from foodie import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^vendors/', views.vendors, name='vendors'),
    url(r'^events/', views.events, name='events'), 
    url(r'^event/(?P<event_id>\d+)/$', views.event, name='singleEvt'),
    url(r'^vendor/(?P<vendor_id>\d+)/$', views.vendor, name='singleVendor')
)


# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'ginger.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#     url(r'^$', include('foodie.urls')),
#     url(r'^vendors/', include('foodie.urls')),
#     #url(r'^admin/', include(admin.site.urls)),

# )
