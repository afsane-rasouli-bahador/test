from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import CreateTodoForm, UserRegisterForm, UpdateTodoForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def Home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {"todos":todos})



def detail(request, todo_id):
    todo = get_object_or_404(Todo, id = todo_id)
    return render(request, 'detail.html', {'todo': todo})



def delete(request, todo_id):
    Todo.objects.get(id = todo_id).delete()
    messages.success(request, 'user todo successfully deleted', extra_tags='success')
    return redirect('home')


def update(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    if request.method == 'POST':
        form = UpdateTodoForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'your todo successfully updated', extra_tags='success')    
            return redirect('home')      
    else:
        form = UpdateTodoForm(instance=todo)
    return render(request, 'update.html', {'update_form': form})




def CreateTodo(request):
    if request.method == 'POST':
        form = CreateTodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'your todo successfully created', extra_tags='success')
            return redirect('home')
    else:
        form = CreateTodoForm()
    return render(request, 'create.html', {'form':form})




def UserRegister(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username = cd['username'], email = cd['email'], password = cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, 'your account successfully created', 'success')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})



def UserLogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully', 'success')
                return redirect('home')
            else:
                messages.error(request, 'uesrname or password is wrong ...')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form':form})



def UserLogout(request):
    logout(request)
    messages.success(request, 'logged out successfully', 'success')
    return redirect('home')