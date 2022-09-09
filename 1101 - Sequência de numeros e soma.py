while True:
    a, b = map(int, input().split())

    if a <= 0 or b <= 0:
        break

    # if a > b:
    #     a, b = b, a
    # l = list(range(a, b+1))

    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a

    lista = list(range(menor, maior + 1))
    soma = 0
    for n in lista:
        print(n, end=' ')
        soma += n

    # print(*lista, end=' ')
    print(f'Sum={soma}')