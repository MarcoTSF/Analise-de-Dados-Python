altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    categoria = "Peso normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
elif 30 <= imc < 34.9:
    categoria = "Obesidade Grau 1"
elif 35 <= imc < 39.9:
    categoria = "Obesidade Grau 2"
else:
    categoria = "Obesidade Grau 3"

print(f"Seu IMC é {imc:.2f}, e você está na categoria: {categoria}.")