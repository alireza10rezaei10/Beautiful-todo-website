from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import deadlines
from django.core import serializers
from .today import Today
import os
# Create your views here.

def loginuser(request):
    if request.method == 'POST': 
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user != None:
            login(request, user)
            return redirect(mainpage)
        else:
            return render(request, 'base/login.html', {'msg': 'Error'})

    else:
        if request.user.is_authenticated:
            return redirect(mainpage)
        else:
            return render(request, 'base/login.html')


@login_required
def logoutuser(request):
    logout(request)
    return redirect(loginuser)


@login_required
def adddeadline(request):
    if request.method == 'POST':
        new_deadline = deadlines(title=request.POST['title'], hour=request.POST['hour'], day=request.POST['day'], month=request.POST['month'], year=request.POST['year'])
        new_deadline.user = request.user
        new_deadline.save()
        return redirect(mainpage)
    else:
        return redirect(mainpage)


@login_required
def delete_deadline(request, deadline_id):
    deadline = get_object_or_404(deadlines, pk=deadline_id, user=request.user)
    if request.method == 'GET':
        return redirect(mainpage)
    else:    
        deadline.delete()
        return redirect(mainpage)


@login_required
def editdeadline(request, deadline_id):
    deadline = get_object_or_404(deadlines, pk=deadline_id, user=request.user)
    if request.method == 'GET':
        return redirect(mainpage)
    else:
        deadline.title = request.POST['title']
        deadline.hour = request.POST['hour']
        deadline.day = request.POST['day']
        deadline.month = request.POST['month']
        deadline.year = request.POST['year']
        deadline.save()
        return redirect(mainpage)


@login_required
def changeprofilepic(request):
    if request.method == 'GET':
        return redirect(mainpage)
    else:
        request.user.profile.avatar.delete()
        request.user.profile.avatar = request.FILES['avatar']
        request.user.profile.save()
        return redirect(mainpage)


@login_required
def mainpage(request):
    deadls = serializers.serialize('json', deadlines.objects.filter(user=request.user).order_by('year', 'month', 'day', 'hour'))
    print(type(deadls))
    return render(request, 'base/newmainpage.html', {'deadlines': deadls, 'today': Today()})
