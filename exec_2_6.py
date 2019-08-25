print('''Tipo da Carne
[1] File Duplo
[2] Alcatra
[3] Picanha''')
opcao = str(input('Qual tipo de carne? '))
qtkg = float(input('Qual a quantidade? '))
total = float

if opcao == '1':
    if (qtkg <= 5):
        total = qtkg * 4.90
    else:
        total = qtkg * 5.80
    print('O tipo da carne: File Duplo  Quantidade {}  Total {}'.format(qtkg, total))
elif opcao == '2':
    if (qtkg <= 5):
        total = qtkg * 5.90
    else:
        total = qtkg * 6.80
    print('O tipo da carne: Alcatra  Quantidade {}  Total {}'.format(qtkg, total))
elif opcao == '3':
    if (qtkg <= 5):
        total = qtkg * 6.90
    else:
        total = qtkg * 7.80
    print('O tipo de carne: Picanha  Quantidade {}  Total {}'.format(qtkg, total))

else:
    print('Opcao invalida')

ct = str(input('Pagar com cartao Tabajara (S/N): '))
desc = 0.0
if ct == 'S':
    desc = total * 0.05
    print('Valor a pagar R$ ', (total - desc))
else:
    print('Valor a pagar R$ {}'.format(total))

