nome = input()
salario_fixo = float(input())
qtd_vendas = float(input())
bonus = float(qtd_vendas * (15/100))
total = salario_fixo + bonus

print(f"TOTAL = R$ {total:.2f}")