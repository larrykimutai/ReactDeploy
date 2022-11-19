from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .views import (ProjectsListView,
ProjectsDetailView,
ProjectsUpdateView,
ProjectsDeleteView)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('view/', ProjectsListView.as_view(), name='project-view'),
    path('', views.home, name='project-home'),
    path('create/', views.create_project, name='project-create'),
    path('view/donate', views.create, name='project-donate'),
    path('about', views.about, name='project-about'),
    path('view/<int:pk>', ProjectsDetailView.as_view(), name='project-detail'),
    path('view/<int:pk>/update', ProjectsUpdateView.as_view(), name='project-update'),
    path('view/<int:pk>/delete', ProjectsDeleteView.as_view(), name='project-delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)