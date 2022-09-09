qtd_pessoas = input()
identificadores_na_fila = input().split()
qtd_sairam = input()
indificadores_sairam = input().split()

for i in indificadores_sairam:
  identificadores_na_fila.remove(i)

fila_final = " ".join(identificadores_na_fila)
print(fila_final)