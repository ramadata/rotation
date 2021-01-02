"""rotation URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('frontend.urls')),
<<<<<<< HEAD
<<<<<<< HEAD
    path('spotify/', include('spotify.urls')),
] 
=======
<<<<<<< HEAD
]
=======
    path('spotify/', include('spotify.urls')),
] 
>>>>>>> c6e2a7fd... added spotify api
>>>>>>> 9ae9138d... added spotify api
=======
    path('spotify/', include('spotify.urls')),
] 
>>>>>>> 6d3401ba... updated views and urls
