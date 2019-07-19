# pylint: disable=no-member
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.forms import User, UserCreationForm
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from .models import Project, Issue
from todo.forms import ProjectForm

class HomeView(TemplateView):
    template_name = 'home.html'

class SignUpView(CreateView):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'registration/signup.html', {'form':form})

class IndexView(ListView):

    def get(self, request):
        projects = Project.objects.all()
        #import pdb;
        #pdb.set_trace()
        return render(request, 'index.html', {'projects': projects})

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        data={
            'title':self.object.title, 
            'description':self.object.description, 
            'updated_at':self.object.updated_at, 
            'created_at':self.object.created_at,
        }
        context['form']=ProjectForm(data)
        return self.render_to_response(context)

class ProjectCreatView(CreateView):

    def get(self, request):
        form = ProjectForm()
        return render(request, 'project_form.html', {'form':form})

    def post(self,request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            Project.objects.create(title=title, description=description)
            return redirect('index')
        return render(request, 'project_form.html', {'form':form})

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ('title', 'description',)
    template_name = 'project_update.html'

    def form_valid(self, ProjectForm):
        project = ProjectForm.save()
        project.updated_at = timezone.now()
        project.save()
        return redirect('index')

class ProjectDeleteView(DeleteView):
    model = Project
    fields = ('title', 'description',)
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('index')