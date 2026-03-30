"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from . import views
import os
from django.http import JsonResponse

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboards', views.LeaderboardViewSet)

# Helper endpoint to show the API base URL using $CODESPACE_NAME
def api_base_url(request):
    codespace_name = os.environ.get('CODESPACE_NAME', '')
    if codespace_name:
        url = f'https://{codespace_name}-8000.app.github.dev/api/'
    else:
        url = 'http://localhost:8000/api/'
    return JsonResponse({'api_base_url': url})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', views.api_root, name='api_root'),
    path('api/base-url/', api_base_url, name='api_base_url'),
]
