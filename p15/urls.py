"""p15 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_topic/',views.create_topic,name="add_topic"),
    path('add_webpage/',views.create_webpage,name="add_webpage"),
    path('display_topic/',views.display_topics,name="display_topics"),
    path('display_topic/<id>',views.display_topic,name="display_topic"),
    path('display_web/',views.display_webpages,name="display_webpages"),
    path('display_web/<webid>',views.display_webpage,name="display_webpage"),
    path('search_web/',views.search_webpage,name="search_web"),
    path('update/topic/<id>',views.update_topic,name="update_topic"),
    path('update/webpage/<id>',views.update_webpage,name="update_webpage"),
    path('delete/topic/<id>',views.delete_topic,name="delete_topic"),
    path('disp_img/<id>',views.disp_img,name="disp_img"),
    path('topic_form/',views.topic_modelform,name="topicmodel_form"),
    path('webform/',views.webform,name="webform"),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)