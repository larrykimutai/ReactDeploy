from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    contract = models.CharField(max_length=100, default="#")
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk':self.pk})

class Image(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='imageSet')
    image = models.ImageField(default='default_project.jpg', upload_to='project_pics')