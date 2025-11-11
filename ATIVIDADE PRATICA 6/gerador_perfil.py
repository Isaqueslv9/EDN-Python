import requests

print("GERADOR DE PERFIL DE USUÁRIO")


def gerar_usuario_aleatorio():
 
    try:
        url = "https://randomuser.me/api/"
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            usuario = dados['results'][0]
            
            perfil = {
                'nome': f"{usuario['name']['first']} {usuario['name']['last']}",
                'email': usuario['email'],
                'pais': usuario['location']['country']
            }
            
            return perfil
        else:
            return None
    except Exception as e:
        print(f"Erro ao consultar API: {e}")
        return None

print("Gerando perfil aleatório...\n")
perfil = gerar_usuario_aleatorio()

if perfil:
    print(f"Nome: {perfil['nome']}")
    print(f"Email: {perfil['email']}")
    print(f"País: {perfil['pais']}")
else:
    print("Não foi possível gerar o perfil.")