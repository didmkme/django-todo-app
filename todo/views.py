# pylint: disable=no-member
from django.utils import timezone
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import User, UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login

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
    model = User
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['project'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    # def get(self, request):
    #     form = UserCreationForm()
    #     return render(request, 'registration/signup.html', {'form': form})

    # def post(self, request):
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    #     return render(request, 'registration/signup.html', {'form':form})

class IndexView(ListView):

    def get(self, request, pk):
        projects = Project.objects.filter(user_id=pk)
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

    def get(self, request, pk):
        form = ProjectForm()
        return render(request, 'project_form.html', {'form':form})

    def post(self,request, pk):
        form = ProjectForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            user = User.objects.get(id=pk)
            Project.objects.create(user=user, title=title, description=description)
            return redirect(reverse('index', kwargs={'pk':pk}))
        return render(request, 'project_form.html', {'form':form})

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ('title', 'description')
    template_name = 'project_update.html'

    def post(self, request, pk):
        form=ProjectForm(request.POST)
        if form.is_valid():
            project=Project.objects.get(id=pk)
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            project.title=title
            project.description=description
            project.save()
            return redirect(reverse('project-detail', kwargs={'pk':pk}))
        return render(request, 'project_update.html', {'form':form})

class ProjectDeleteView(DeleteView):
    model = Project
    fields = ('title', 'description',)
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('home')