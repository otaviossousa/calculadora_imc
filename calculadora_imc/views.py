from django.shortcuts import render

def calculadora_imc(request):
    imc = None
    classificacao = ''
    if request.method == 'POST':
        altura = float(request.POST['altura'].replace(',', '.'))
        peso = float(request.POST['peso'].replace(',', '.'))
        imc = peso / (altura ** 2)
        if imc < 18.5:
            classificacao = 'Magreza'
        elif 18.5 <= imc < 24.9:
            classificacao = 'Normal'
        elif 25 <= imc < 29.9:
            classificacao = 'Sobrepeso'
        else:
            classificacao = 'Obesidade'
    return render(request, 'calculadora_imc.html', {'imc': imc, 'classificacao': classificacao})