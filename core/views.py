from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = 'index.html'
    context = {
        'mensagem': 'Bem vindo a aplicaçao'
    }
    return render(request, template_name, context)