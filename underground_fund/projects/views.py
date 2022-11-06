from django.shortcuts import render
from .models import Projects
from django.views.generic import (ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ProjectsListView(ListView):
    model = Projects
    template_name = 'projects/view-project.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class ProjectsDetailView(DetailView):
    model = Projects

class ProjectsCreateView(LoginRequiredMixin,CreateView):
    model = Projects
    fields = ['title','description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProjectsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Projects
    fields = ['title','description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

def view(request):
    return render(request, "projects/view-project.html")


def create(request):
    context = {
        'posts': Projects.objects.all()
    }
    return render(request,'blog/home.html', context)

def projects(request):
    context = {
        'posts': Projects.objects.all()
    }
    return render(request,'projects/view-project.html', context)


def about(request):
    return render(request, "projects/about.html")

def home(request):
    return render(request, "projects/home.html")