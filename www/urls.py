from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views import static ##新增
from django.conf import settings ##新增
from django.urls import re_path as url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),

    path('blog/', include('blog.urls')),
    #path('about/', include('blog.urls')),
    path('comment/', include('comment.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^static/(?P<path>.*)$', static.serve,
      {'document_root': settings.STATIC_ROOT}, name='static'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'www.views.page_not_found'
handler500 = 'www.views.server_error'
