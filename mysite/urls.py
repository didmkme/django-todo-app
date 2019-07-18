"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from todo import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),

    #http://127.0.0.1:8000/projects/
    path('projects/', views.IndexView.as_view(), name='index'),

    #http://127.0.0.1:8000/new/
    path('new/', views.ProjectCreatView.as_view(), name = 'project-create'),

    #http://127.0.0.1:8000/projects/1/
    path('<int:pk>/', views.ProjectDetailView.as_view(), name = 'project-detail'),
    
    #http://127.0.0.1:8000/projects/1/edit/
    path('<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project-update'),

    path('<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project-delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
