print("=-" * 40)
print("CONVERSOR DE MOEDAS")
print("=-" * 40)

valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolares = valor_reais / taxa_dolar
valor_euros = valor_reais / taxa_euro

print(f"Valor em Reais: R$ {valor_reais:.2f}")
print(f"Taxa do Dolar: R$ {taxa_dolar:.2f}")
print(f"Taxa do Euro: R$ {taxa_euro:.2f}")
print(f"Valor em Dolares: $ {valor_dolares:.2f}")
print(f"Valor em Euros: € {valor_euros:.2f}")

