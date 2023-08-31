"""
URL configuration for library_project project.

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
from django.urls import path, include
from rest_framework import routers
from library_app.views import AuthorView, AddressView, StudentView, BookView, BookIssuedView, BookReturnedView
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('authors', AuthorView ,'authors')
router.register('address', AddressView ,'address')
router.register('students', StudentView, 'students')
router.register('books', BookView, 'books')
router.register('bookissued', BookIssuedView, 'bookissued')
router.register('bookreturned', BookReturnedView, 'bookreturned')





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
