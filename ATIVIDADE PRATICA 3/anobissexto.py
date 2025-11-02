print("VERIFICADOR DE ANO BISSEXTO")
print("=-" * 40)

ano = int(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} e um ano bissexto.")
else:
    print(f"{ano} nao e um ano bissexto.")