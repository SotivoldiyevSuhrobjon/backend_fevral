from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Todo
from django.db.models import Q

def register_page(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('card_list')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            context['error'] = 'Bunday username mavjud'
            return render(request, 'register.html', context)

        if password == password2:
            user = User.objects.create(username=username, password=password)
            user.set_password(password)
            user.save()
            return redirect('task_list')
        else:
            context['error'] = 'Parol bir xil emas'
    return render(request, 'register.html')


def login_page(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('card_list')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            context['error'] = 'Bunday foydalanuvchi mavjud emas!'
            return render(request, 'login.html', context)

    return render(request, 'login.html', context)


@login_required
def card_list(request):
    q = request.GET.get('q')
    tasks = Todo.objects.filter(user=request.user)

    if q is not None:
        tasks = tasks.filter(Q(title__icontains=q))
        
    context = {
        'user_tasks_count': tasks.count(),
        'tasks': tasks,

    }
    return render(request, 'card_list.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def create_card(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        narx = request.POST.get('narx')
        sifat = request.POST.get('sifat')
        task = Todo.objects.create(
            user= request.user,
            title=title,
            description=description,
            narx=narx,
            sifat=sifat,    
        )
        if sifat == 'Alo':
            task.sifat='Alo'
        elif sifat == 'yaxshi':
            task.sifat='yaxshi'
        else:
            task.sifat='orta'
        task.save()

        return redirect('card_list')

    return render(request, 'create_card.html')


@login_required
def detail_btn(request, pk):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        # complated = request.POST.get('complated')
        narx = request.POST.get('narx')
        sifat = request.POST.get('sifat')
        task = Todo.objects.get(pk=pk)
        task.title = title
        task.description = description
        task.narx = narx
        task.sifat = sifat
        task.save()
        return redirect('card_list')


    task = get_object_or_404(Todo, pk=pk)
    context = {
        'task': task,
    }
    return render(request, 'detail_btn.html', context)
