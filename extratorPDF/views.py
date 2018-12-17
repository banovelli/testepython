from django.shortcuts import render

def extrair_tabela(request):
    return render(request, 'extratorPDF/extrair_tabela.html', {})
