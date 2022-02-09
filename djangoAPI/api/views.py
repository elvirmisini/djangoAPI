from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.renderers import JSONRenderer
from .models import Task
from .serializers import TaskSerializer
from datetime import date
from .forms import CreateTask
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
import requests

@csrf_exempt
def task_list(request):

    if request.method == 'GET':
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def task_detail(request, pk):

    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=204)

@csrf_exempt
def task_update(request, pk):

    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def task_delete(request, pk):

    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    serializer = TaskSerializer(task)
    deletedOne = JsonResponse(serializer.data)
    if task.delete():
        return deletedOne
    return HttpResponse(status=204)

@csrf_exempt
def task_today(request):
        tasks = Task.objects.filter(date__date=date.today())
        return render(request,'index.html',{'tasks':tasks})

@csrf_exempt
def front(request):
    tasks = Task.objects.filter(date__date=date.today())
    return render(request,'front.html',{'tasks':tasks})

@csrf_exempt
def report(request):
        tasks = Task.objects.all()
        return render(request,'report.html',{'tasks':tasks})

# class AddTask(CreateView):
#     model = Task
#     template_name = 'addTask.html'
#     fields = ['title']
#
@csrf_exempt
def AddTask(request):

        if request.method=='POST':
            title=request.POST.get('title')
            if title:
                data = FormParser().parse(request)
                data = JSONRenderer().render(data)
                requests.post(url=f'http://127.0.0.1:8000/task/',data=data)
                return redirect('home')

        tasks=Task.objects.filter(is_done=False)
        return render(request,'front.html',{'tasks':tasks})
# class EditTask(UpdateView):
#         model = Task
#         template_name = 'edit.html'
#         fields = ['title']

def EditTask(request,pk):

    pk = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = CreateTask(request.POST, instance=pk)
        requests.post(url=f'http://127.0.0.1:8000/task/{pk}/update/')
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreateTask(instance=pk)
        return render(request, 'edit.html', {'form': form})

# class DeleteTask(DeleteView):
#     model = Task
#     template_name = 'delete.html'
#     fields = ['title']
#     success_url = reverse_lazy('home')

def DeleteTask(request, pk):
    # requests.delete(url=f'http://127.0.0.1:8000/task/{pk}/')
    # return redirect("home")

    if request.is_ajax():
        requests.delete(url=f'http://127.0.0.1:8000/task/{pk}/')
        return JsonResponse({"message": "success"})
    return JsonResponse({"message": "Wrong request"})