from posixpath import split

print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

par = []
impar = []

if a % 2 == 0: par.append(a)
if b % 2 == 0: par.append(b)
if c % 2 == 0: par.append(c)
if d % 2 == 0: par.append(d)

if a % 2 != 0: impar.append(a)
if b % 2 != 0: impar.append(b)
if c % 2 != 0: impar.append(c)
if d % 2 != 0: impar.append(d)


print(f"Soma dos números pares = {sum(par)}")
print(f"Soma dos números impares = {impar}")