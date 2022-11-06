from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .views import (ProjectsListView,
ProjectsDetailView,
ProjectsCreateView,
                    ProjectsUpdateView)

urlpatterns = [
    path('view/', ProjectsListView.as_view(), name='project-view'),
    path('', views.home, name='project-home'),
    path('create/', views.create, name='project-create'),
    path('view/donate', views.create, name='project-donate'),
    path('about', views.about, name='project-about'),
    path('view/<int:pk>', ProjectsDetailView.as_view(), name='project-detail'),
    path('view/new', ProjectsCreateView.as_view(), name='project-create'),
    path('view/<int:pk>/update', ProjectsUpdateView.as_view(), name='project-update')
]

urlpatterns += staticfiles_urlpatterns()