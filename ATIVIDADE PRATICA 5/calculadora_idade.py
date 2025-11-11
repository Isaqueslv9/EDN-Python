print("CALCULADORA DE IDADE EM DIAS")
print("=-=" * 40)

def calcular_idade_em_dias(ano_nascimento):
    20
    from datetime import datetime
    
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    
    return idade_dias

ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_dias = calcular_idade_em_dias(ano_nascimento)

print(f"\nIdade aproximada em dias: {idade_dias} dias")
print(f"(Cálculo aproximado considerando 365 dias por ano)")