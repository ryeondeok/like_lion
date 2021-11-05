"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include

from mainapp.views import company_list, mainpage, company_detail , checkbox
from django.conf.urls.static import static
from django.conf import settings  # 배웠을 때는 필요 없어 보였는데 막상 없으니까 아래 static 에서 settings 를 인식하지 못함.

urlpatterns = [
    path('admin/', admin.site.urls), 

    path('', mainpage , name="mainpage"),
    path('company_list/', company_list , name='company_list'),
    path('<int:id>', company_detail , name='company_detail'),
    
    path('company_list/checkbox', checkbox , name="checkbox"),

    path('searchapp/',include('searchapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)