import random
import string
import requests


print("=-=" * 40)
print("GERADOR DE SENHA ALEATÓRIA")
print("=-=" * 40)

def gerar_senha(tamanho):
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
 
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
senha_gerada = gerar_senha(tamanho_senha)

print(f"\nSenha gerada: {senha_gerada}")
