from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from .forms import TarefaForm


# --- CADASTRO DE USUÁRIO ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)  # Login automático após cadastro
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from .forms import TarefaForm

# --- CADASTRO DE USUÁRIO ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


# --- HOME ---
@login_required
def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.user = request.user
            tarefa.save()
            return redirect('home')
    else:
        form = TarefaForm()

    tarefas = Tarefa.objects.filter(user=request.user)

    return render(request, 'home.html', {
        'form': form,
        'tarefas': tarefas,
        'nome_usuario': request.user.username,
    })


# --- CONCLUIR TAREFA ---
@login_required
def concluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    if request.method == 'POST':
        tarefa.concluida = True
        tarefa.save()
        return redirect('home')


# --- DELETAR TAREFA ---
@login_required
def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('home')
