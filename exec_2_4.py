n1 = int(input('Digite o primeiro valor:  '))
n2 = int(input('Digite o segundo valor: '))
soma = float
mult = float

print('''
[1]soma
[2]mult
[3]div
[4]sub''')
opcao = str(input('Escolha uma operacao? '))
if opcao == '1':
    soma = n1 + n2
    if (soma % 2 == 0):
     print('O resultado da soma eh {} e eh PAR '.format(soma))
    else:
     print('O resultado da soma eh {} e eh IMPAR' .format(soma))
elif opcao == '2':
    prod = n1 * n2
    if (prod % 2 == 0):
        print('O resultado da multiplicacao eh {} e eh PAR '.format(prod))
    else:
        print('O resultado da multiplicacao eh {} e eh IMPAR'.format(prod))
elif opcao == '3':
    div = n1/n2
    if (div % 2 == 0):
        print('O resultado d divisao eh {} e eh PAR '.format(div))
    else:
        print('O resultado da divisao eh {} e eh IMPAR'.format(div))
elif opcao == '4':
    sub = n1 - n2
    if (sub % 2 == 0):
        print('O resultado da subtracao  eh {} e eh PAR '.format(sub))
    else:
        print('O resultado da subtracao eh {} e eh IMPAR'.format(sub))
else:
    print('opcao invalida')


