from django.shortcuts import render
from django.shortcuts import HttpResponse

def calc(request,funcao,v1,v2):
    if funcao =='soma':
        return HttpResponse('<h1>O resultado da Soma de {} com {} é igual: {}</h1>'.format(v1,v2,v1+v2))
    elif funcao =='multi':
        return HttpResponse('<h1>O resultado da Multiplicação de {} com {} é igual: {}</h1>'.format(v1,v2,v1*v2))
    elif funcao =='sub':
        return HttpResponse('<h1>O resultado da Subtração de {} com {} é igual: {}</h1>'.format(v1,v2,v1-v2))
    elif funcao =='div':
        if v2 == 0:
            return HttpResponse('<h1>Erro - Divisão por Zero</h1>')
        else:
            return HttpResponse('<h1>O resultado da Divisão de {} com {} é igual: {}</h1>'.format(v1,v2,v1/v2))
        

    

