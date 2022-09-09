qtd = 0
aposta = (input().split(" "))
resultado = (input().split(" "))

for i in resultado:
    if i in aposta:
        qtd = qtd+1

if(qtd == 3):
    print("terno")
elif(qtd == 4):
    print("quadra")
elif(qtd == 5):
    print("quina")
elif(qtd == 6):
    print("sena")
else:
    print("azar")