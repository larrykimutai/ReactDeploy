from django.shortcuts import render
from .models import Projects, Image
from .forms import ProjectForm, ImageForm
from django.views.generic import (ListView,
    DetailView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.contrib import messages

def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        files = request.FILES.getlist("image")
        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user
            f.save()
            for i in files:
                Image.objects.create(project = f, image = i)
            messages.success(request, "New Project added")
            return HttpResponseRedirect("/view")
        else:
            print(form.errors)
    else:
        form = ProjectForm()
        imageForm = ImageForm()

    return render(request, "projects/create_project.html", {"form": form, "imageForm": imageForm})

class ProjectsListView(ListView):
    model = Projects
    template_name = 'projects/view-project.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class ProjectsDetailView(DetailView):
    model = Projects

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['images'] = Image.objects.all()
        return context

class ProjectsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Projects
    fields = [
        'title',
        'description',
        'deadline']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

class ProjectsDeleteView(DeleteView):
    model = Projects
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def create(request):
    context = {
        'posts': Projects.objects.all()
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request, "projects/about.html")

def home(request):
    return render(request, "projects/home.html")