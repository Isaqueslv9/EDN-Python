print("CALCULADORA DE SALÁRIO")
print("=-" * 40)

numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite as horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: "))

salario = horas_trabalhadas * valor_por_hora

print(f"NUMERO = {numero_funcionario}")
print(f"SALARIO = R$ {salario:.2f}")