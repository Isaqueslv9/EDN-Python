print("CLASSIFICADOR DE IDADE")
print("=-" * 40)
idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 12:
    classificacao = "Criança"
elif idade >= 13 and idade <= 17:
    classificacao = "Adolescente"
elif idade >= 18 and idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

print(f"Classificaçao: {classificacao}")