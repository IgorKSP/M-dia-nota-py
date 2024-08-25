nome = input('nome: ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

NotaTotal = (nota1 + nota2)/2

def resultado ():
    foi = 'aprovado' if NotaTotal>7 or notaFinal>5 else "reprovado"
    frase = 'O aluno {0} foi {1}.'.format(nome, foi)
    print(frase)

if (NotaTotal>7):
    resultado()
else:
    exame = float(input('Nota do exame: '))
    notaFinal = (NotaTotal + exame)/2 

    if (notaFinal>5):
        resultado()
    else:
        resultado()       
