n1 = float(input('Digite nota p1:'))
n2 = float(input('Digite nota p2:'))
media = (n1 + n2)/2
if media >= 7.0 and media < 10.0:
    print('Aprovado, media {}'.format(media))
elif media == 10.0:
    print('Aprovado com Distincao')
else:
    print('Reprovado, media {}'.format(media))
