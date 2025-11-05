print("Digite números inteiros")
print("Digite 'fim' quando terminar\n")

contador_pares = 0
contador_impares = 0

while True:
    entrada = input("Digite um número: ")
    
    
    if entrada.lower() == 'fim':
        break
    
    try:
        numero = int(entrada)
        
        
        if numero % 2 == 0:
            print(f"{numero} é PAR")
            contador_pares += 1
        else:
            print(f"{numero} é ÍMPAR")
            contador_impares += 1
            
    except ValueError:
        print("ERRO: Entrada inválida! Digite um número inteiro ou 'fim'.")


print(f"\n--- RESUMO ---")
print(f"Quantidade de números pares: {contador_pares}")
print(f"Quantidade de números ímpares: {contador_impares}")
print(f"Total de números inseridos: {contador_pares + contador_impares}")