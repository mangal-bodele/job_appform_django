from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import JobForm
from .models import Job

@login_required(login_url='login_url')
def add_job(request):
    template_name = 'crud_app/add.html'
    form = JobForm()
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def show_job(request):
    template_name = 'crud_app/show.html'
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, template_name, context)


def update_job(request,pk):
    template_name = 'crud_app/add.html'
    obj=Job.objects.get(id=pk)
    form = JobForm(instance=obj)
    if request.method == "POST":
        form = JobForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def delete_job(request,pk):
    template_name = 'crud_app/confirm.html'
    obj = Job.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
    return render(request, template_name)


