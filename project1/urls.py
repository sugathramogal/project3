"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from .views import home,demo,demo2,demo3,demo4
#from .views import demo3
#from demoapp.views import home,home1
#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home ,name ='home'),
    #path("demo/",demo,name="demo"),
    path("demo2/",demo2,name="demo2"),
    path("demo3/",demo3,name="demo3"),
    path("demo4/",demo4,name="demo4"),
   # path("home1/",home1,name="home1"),
]



urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
