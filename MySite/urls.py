"""
URL configuration for MySite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path

# 必须将所有的地址写在一个urlpatterns里面去，否则找不到路由，那么以下的代码几乎就是没有用的了
urlpatterns = [
    path('admin/', admin.site.urls),
]
# 新增的路由，针对app polls的添加
urlpatterns = [
    path('admin/', admin.site.urls),
    path("polls/", include("polls.urls")),
]
