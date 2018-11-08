"""who_is_who URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from who_is import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.log_in, name='log_in'),
    path('signup', views.sign_up, name='sign_up'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_to, name='logout'),
    path('game/<str:game_id>', views.game, name='game'),
    path('test_ajax/valid/', views.test_ajax, name='test_ajax'),
    path('game-stat/', views.game_stat, name='game_stat'),
    path('test/', views.get_test, name='testt')
]
