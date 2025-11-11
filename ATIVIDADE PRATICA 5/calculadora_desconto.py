print("CALCULADORA DE DESCONTO")
print("=-=" * 40)

preco_produto = float(input("Digite o preço do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

valor_desconto = preco_produto * (percentual_desconto / 100)
preco_final = preco_produto - valor_desconto

print(f"\nPreço original: R$ {preco_produto:.2f}")
print(f"Desconto ({percentual_desconto}%): R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")