# pylint: disable=no-member
from django.utils import timezone
from django.shortcuts import render, redirect, reverse

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from .models import Project, Issue
from todo.forms import IssueForm

class IssueIndexView(ListView):

    def get(self, request, pk):
        issues = Issue.objects.filter(project_id=pk)
        return render(request, 'issue_index.html', {'issues': issues})

class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issue_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        data={
            'project':self.object.project, 
            'title':self.object.title, 
            'open_date':self.object.open_date, 
            'close_date':self.object.close_date,
        }
        context['form']=IssueForm(data)
        return self.render_to_response(context)

class IssueCreateView(CreateView):  

    def get(self, request, pk):
        form = IssueForm()
        return render(request, 'issue_create.html', {'form':form})

    def post(self,request, pk):
        form = IssueForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            open_date = form.cleaned_data['open_date']
            close_date = form.cleaned_data['close_date']
            project = Project.objects.get(id=pk)
            new_issue=Issue.objects.create(project=project, title=title, open_date=open_date, close_date=close_date)
            new_issue.save()

            return redirect(reverse('project-detail', kwargs={'pk':pk}))
        return render(request, 'issue_create.html', {'form':form})

# class IssueUpdateView(UpdateView):
#     model = Issue
#     fields = ('title', 'open_date', 'close_date')
#     template_name = 'issue_update.html'

#     def form_valid(self, ):
#         project = ProjectForm.save()
#         project.updated_at = timezone.now()
#         project.save()
#         return redirect('index')