print("CONVERSOR DE TEMPERATURA")
print("=-" * 40)

temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C/F/K): ").upper()
unidade_destino = input("Digite a unidade de destino (C/F/K): ").upper()


if unidade_origem == "C":
    temp_celsius = temperatura
elif unidade_origem == "F":
    temp_celsius = (temperatura - 32) * 5/9
elif unidade_origem == "K":
    temp_celsius = temperatura - 273.15


if unidade_destino == "C":
    resultado = temp_celsius
elif unidade_destino == "F":
    resultado = (temp_celsius * 9/5) + 32
elif unidade_destino == "K":
    resultado = temp_celsius + 273.15

print(f"Resultado: {resultado:.2f}°{unidade_destino}")


