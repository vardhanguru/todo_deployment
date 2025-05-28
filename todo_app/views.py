from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .forms import TodoForm
from .models import Todo

# Create your views here.
@never_cache
def home_view(request):
    if not request.user.is_authenticated:
        print("here")
        return redirect('auth')

    task = TodoForm()
    if request.method=='POST':
        task = TodoForm(request.POST)
        if task.is_valid():
            task = task.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
            
    tasks = Todo.objects.filter(user = request.user)



    return render(request, 'home.html', context={'form':task, 'tasks':tasks})

def auth_view(request):


    if request.method=="POST":
        print("inside the post method")
        print(request.POST)
        if 'login' in request.POST:
            username = request.POST.get('username')

            password = request.POST.get('password')

            if '@' in username:
                print("consider this as email")

                user = authenticate(request, email=email, password=password)
                print("authenticated")
                login(request, user)
                return redirect('home')
            else:
                print("consider this as username")
                user = authenticate(request, username=username, password=password)
                print("authenticated")
                login(request, user)
                return redirect('home')


        elif 'register' in request.POST:
            print("inside register code")
            print(request.POST)
            name = request.POST.get('name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if User.objects.filter(username=username).exists():
                messages.error(request, "something went wrong, username is already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "email already taken")
            else:
                if password!=confirm_password:
                    messages.error(request, "password and confirm password are not same")
                else:
                    user = User.objects.create_user(username=username, email=email, password=password,first_name = name)
                    user.save()
                    messages.success(request, "User registration is successfull, Please login")


                






    return render(request, 'auth.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('auth')


@login_required
def update_view(request, taskid):
    task = get_object_or_404(Todo, id=taskid, user=request.user)
    print(task)
    form = TodoForm( instance=task)
    if request.method=="POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            task.task = form.cleaned_data['task']
            task.description = form.cleaned_data['description']
            task.save()
            return redirect('home')
            
    return render(request, 'update.html', {'form':form})


def base_view(request):
   
   if request.user.is_authenticated:
       return redirect('home')
   else:
       return redirect('auth')
   

def delete_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id)

    if request.method=='POST':
        task.delete()
    
    return redirect('home')

def toggle_view(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    print("inside toggle view")
    if request.method=='POST':
        print("post method")
        task.is_completed = not task.is_completed
        task.save()

    return redirect('home')

    
