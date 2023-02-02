from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages

from payments.models import Groups_Pay
from payments.forms import GroupsForm
from expenses.models import Payout
from expenses.forms import PayoutForm

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('index')


@login_required
def signout(request):
    logout(request)
    return redirect('index')

@login_required 
def settings(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserChangeForm( postdata, instance=request.user )
        if form.is_valid():
            form.save()
            form.clean()
        return redirect("index")
    else:
        form = UserChangeForm(initial={
            'username':request.user.username,
            'first_name':request.user.first_name,
            'last_name':request.user.last_name,
            })
        return render(request, 'update.html', {"form": form})

@login_required
def create_groups(request, pk):
    if request.method == "GET":
        print(pk)
        if pk==str(999):
            return render(request, 'create_groups.html', {"form": GroupsForm})
        task = get_object_or_404(Groups_Pay, id=pk, user=request.user)
        form = GroupsForm(instance=task)
        return render(request, 'create_groups.html', {'form': form})
    else:
        try:
            if pk==str(999):
                form = GroupsForm(request.POST)
                new_task = form.save(commit=False)
                new_task.user = request.user
                new_task.save()
                return redirect('/create_groups/999')

            task = get_object_or_404(Groups_Pay, pk=pk, user=request.user)
            form = GroupsForm(request.POST, instance=task)
            form.save()
            return redirect('/create_groups/999')
        except ValueError:
            return render(request, 'create_groups.html', {"form": GroupsForm, "error": "Error creating groups."})
    

@login_required
def delete_task(request, pk):
    group = get_object_or_404(Groups_Pay, id=pk)
    group.delete()
    return redirect('groups')

    

@login_required
def groups_payout(request):
    groups = Groups_Pay.objects.filter(user=request.user)
    return render(request, 'groups_payout.html', {"groups": groups})


@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Groups_Pay, id=task_id, user=request.user)
        form = GroupsForm(instance=task)
        return render(request, 'create_groups.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Groups_Pay, pk=task_id, user=request.user)
            task.pk = task_id
            form = GroupsForm(request.POST, instance=task)
            form.save()
            return redirect('create_groups')
        except ValueError:
            return render(request, 'create_groups.html', {'task': task, 'form': form, 'error': 'Error updating groups.'})