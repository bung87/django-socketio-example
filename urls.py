import os
from django.conf.urls import patterns,include
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import admin
urlpatterns = patterns('',
    (r'^$', TemplateView.as_view(template_name="chat.html")),
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': os.path.join(settings.BASE_PATH, 'media')}),
)

urlpatterns += patterns('views',
    (r'^socket\.io', 'socketio'),
)
