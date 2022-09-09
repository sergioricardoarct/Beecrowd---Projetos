while(True):
    a, b = input().split()
    if(a == '0' and b == '0'):
        break
    soma = int(a) + int(b)
    valor_string = int(str(soma).replace('0',''))
    print(valor_string)