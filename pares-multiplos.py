numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0 and numero % 3 == 0:
    print(f"O número {numero} é simultaneamente par e múltiplo de 3.")
else:
    print(f"O número {numero} não atende à condição de ser simultaneamente par e múltiplo de 3.")