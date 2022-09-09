num = input().split()
a, b = num

a = int(num[0])
b = int(num[1])

if a < b:
    tempo = b - a
else:
    tempo = (24 - a) + b
print('O JOGO DUROU {} HORA(S)'.format(tempo))