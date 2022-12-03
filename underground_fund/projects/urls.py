from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .views import (ProjectsListView,
ProjectsDetailView,
ProjectsUpdateView,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('view/', ProjectsListView.as_view(), name='project-view'),
    path('', views.home, name='project-home'),
    path('create/', views.create_project, name='project-create'),
    path('view/donate', views.create, name='project-donate'),
    path('about', views.about, name='project-about'),
    path('view/<int:pk>', ProjectsDetailView.as_view(), name='project-detail'),
    path('view/<int:pk>/update', views.update_project, name='project-update')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
