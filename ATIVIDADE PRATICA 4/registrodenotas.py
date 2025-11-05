print("=-= REGISTRO DE NOTAS =-=")
print("Digite as notas dos alunos (0 a 10)")
print("Digite 'fim' quando terminar")

notas = []

while True:
    entrada = input("Digite uma nota: ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if nota < 0 or nota > 10:
            print("ERRO: Nota inválida! Digite um valor entre 0 e 10.")
            continue
        notas.append(nota)
        print(f"Nota {nota} registrada com sucesso!")
        
    except ValueError:
        print("ERRO: Entrada inválida! Digite um número ou 'fim'.")


if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"\n--- RESULTADO ---")
    print(f"Total de notas registradas: {len(notas)}")
    print(f"Média da turma: {media:.2f}")
else:
    print("\nNenhuma nota foi registrada.")