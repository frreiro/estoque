from django.shortcuts import render, redirect
from .models import Saidas
from .forms import SaidaForm

# Create your views here.
def list_saida(request):
    saidas = Saidas.objects.all()
    template_name = 'list_saida.html'
    context = {
        'saidas': saidas
    }
    return render(request, template_name, context)


def new_saida(request):
    if request.method == 'POST':
        form = SaidaForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade - form.cleaned_data['quantidade']
            form.cleaned_data['produto'].save_base()
            form.save()
            return redirect('saida:list_saida')
    
    else:
        template_name = 'new_saida.html'
        context = {
            'form': SaidaForm()
        }
        return render(request, template_name, context)
