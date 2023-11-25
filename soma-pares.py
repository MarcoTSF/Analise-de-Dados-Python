N = int(input("Digite um número inteiro positivo: "))

if N <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    soma = 0

for i in range(2, N+1, 2):
    soma += i

print(f"A soma dos números pares de 1 até {N} é: {soma}")