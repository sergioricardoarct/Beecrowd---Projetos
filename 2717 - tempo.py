expediente_restante = int(input())
tempo_presente_1, tempo_presente_2 = input().split()

if(int(tempo_presente_1)+int(tempo_presente_2) <= expediente_restante):
  print('Farei hoje!')
else:
  print('Deixa para amanha!')