peca_01 = input().split()
peca_02 = input().split()
valor_total = int(peca_01[1])*float(peca_01[2]) + int(peca_02[1])*float(peca_02[2])

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")