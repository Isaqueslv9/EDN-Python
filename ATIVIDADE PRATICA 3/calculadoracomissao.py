print("CALCULADORA DE COMISSAO")
print("=-" * 40)

nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salario fixo: "))
total_vendas = float(input("Digite o total de vendas: "))

comissao = total_vendas * 0.15
total_receber = salario_fixo + comissao

print(f"TOTAL = R$ {total_receber:.2f}")