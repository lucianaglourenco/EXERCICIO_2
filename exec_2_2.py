n1 = float(input('Digite nota p1:'))
n2 = float(input('Digite nota p2:'))
media = (n1 + n2)/2
if media >= 7.5 and media < 9.0:   print(' Nota 1 {} Nota 2 {} media {} conceito A Aprovado'.format(n1,n2,media))
elif media >= 6.0 and media <7.5 :
    print(' Nota1 {} Nota2 {} media {} conceito B Aprovado'.format(n1,n2,media))
elif media >= 4.0 and media <6.0 :
    print(' Nota1 {} Nota2 {} media {} conceito C Aprovado'.format(n1,n2,media))
elif media > 4.0 and media < 0.0:
    print(' Nota1 {} Nota2 {} media {} conceito D Reprovado'.format(n1, n2, media))
else:
    print(' Nota1 {} Nota2 {} media {} conceito D Reprovado'.format(n1, n2, media))
