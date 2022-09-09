a = []
for i in range(5):
  n = int(input())
  a.append(int(n))

num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
for j in range(5):
  if a[j] % 2 == 0:
    num_1 += 1
  if a[j] % 2 == 1:
    num_2 += 1
  if a[j] > 0:
    num_3 += 1
  if a[j] < 0:
    num_4 += 1
print(num_1, "valor(es) par(es)")
print(num_2, "valor(es) impar(es)")
print(num_3, "valor(es) positivo(s)")
print(num_4, "valor(es) negativo(s)")