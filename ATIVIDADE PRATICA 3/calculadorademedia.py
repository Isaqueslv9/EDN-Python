print("CALCULADORA DA MÉDIA")
print("=-" * 40)

N1 = float(input("Digite a nota N1: "))
N2 = float(input("Digite a nota N2: "))
N3 = float(input("Digite a nota N3: "))
N4 = float(input("Digite a nota N4: "))

media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input("Digite a nota do exame: "))
    print(f"Nota do exame: {nota_exame:.1f}")
    
    media_final = (media + nota_exame) / 2
    
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media_final:.1f}")