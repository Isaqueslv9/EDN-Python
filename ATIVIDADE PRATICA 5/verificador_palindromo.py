print("2. VERIFICADOR DE PALÍNDROMO")
print("=" * 40)

def palindromo(texto):
    
    texto_limpo = ""
    for char in texto.lower():
        if char.isalnum():
            texto_limpo += char
    
    return texto_limpo == texto_limpo[::-1]

texto = input("Digite uma palavra ou frase: ")
resultado = palindromo(texto)

if resultado:
    print("Sim, e um palíndromo")
else:
    print("Não e um palíndromo")