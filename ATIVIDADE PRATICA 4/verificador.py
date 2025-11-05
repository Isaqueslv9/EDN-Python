print("Uma senha forte deve ter:")
print("- Pelo menos 8 caracteres")
print("- Pelo menos um número")
print("Digite 'sair' para cancelar\n")

while True:
    senha = input("Digite uma senha: ")
    
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break
    
    if len(senha) < 8:
        print("ERRO: Senha muito curta! Deve ter pelo menos 8 caracteres.")
        print()
        continue
    
    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break
    
    if not tem_numero:
        print("ERRO: A senha deve conter pelo menos um número!")
        print()
        continue
    
    print("\n✓ Senha forte! Senha aceita com sucesso.")
    break