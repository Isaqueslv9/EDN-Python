print("CALCULADORA DE GORJETA")
print("=-=" * 40)

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

valor_conta = float(input("Digite o valor da conta: R$ "))
porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta (%): "))

gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
total_pagar = valor_conta + gorjeta

print(f"\nValor da gorjeta: R$ {gorjeta:.2f}")
print(f"Total a pagar: R$ {total_pagar:.2f}")
