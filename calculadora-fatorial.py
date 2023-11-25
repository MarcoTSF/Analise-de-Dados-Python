def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

numero = int(input("Digite um número para calcular o fatorial: "))

if numero < 0:
    print("Não existe fatorial para números negativos.")
else:
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}.")