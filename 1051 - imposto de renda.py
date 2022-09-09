salario = float(input())

if salario <= 2000.00:
    imposto = 0
    print('Isento')

if 2000.00 < salario <= 3000.00:
    salario_8 = salario - 2000.00
    imposto = salario_8 * (8 / 100)

if 3000.00 < salario <= 4500.00:
    imposto_8 = (8 / 100) * (1000.00)
    salario_18 = salario - 3000.00
    imposto = salario_18 * (18 / 100) + imposto_8

if salario > 4500.00:
    imposto_8 = (8 / 100) * (1000.00)
    imposto_18 = (18 / 100) * (1500.00)
    salario_28 = salario - 4500.00
    imposto = imposto_18 + imposto_8 + salario_28 * (28 / 100)

if salario > 2000.00:
    imposto = float(imposto)
    print(f"R$ {imposto:.2f}")