print(" CALCULADORA DE DESCONTO")
print("=-" * 40)

nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

valor_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_desconto

print(f"Produto: {nome_produto}")
print(f"Preco original: R$ {preco_original:.2f}")
print(f"Desconto: {percentual_desconto}%")
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preco Final: R$ {preco_final:.2f}")