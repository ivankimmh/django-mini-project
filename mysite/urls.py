"""
URL configuration for mysite project.

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
from bookmark.views import BookmarkLV, BookmarkDV
from mysite.views import HomeView, UserCreateView, UserCreateDoneTV
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/register/', UserCreateView.as_view(), name='register'),
    path('account/register/done/', UserCreateDoneTV.as_view(), name='register_done'),

    # bookmark
    # path('bookmark/', include('bookmark.urls')),

    # bookmark - class-based views
    path('bookmark/', BookmarkLV.as_view(), name='index'),
    path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),

    # blog
    path('blog/', include('blog.urls')),

    # photo
    path('photo/', include('photo.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
