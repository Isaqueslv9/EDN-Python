import requests

print("CONSULTA DE CEP (ViaCEP)")


def consultar_cep(cep):
    
    try:
        
        cep_limpo = cep.replace("-", "").replace(".", "")
        
        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            
            if 'erro' not in dados:
                return dados
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"Erro ao consultar CEP: {e}")
        return None

cep = input("Digite o CEP (ex: 01310-100): ")
endereco = consultar_cep(cep)

if endereco:
    print(f"\nLogradouro: {endereco.get('logradouro', 'N/A')}")
    print(f"Bairro: {endereco.get('bairro', 'N/A')}")
    print(f"Cidade: {endereco.get('localidade', 'N/A')}")
    print(f"Estado: {endereco.get('uf', 'N/A')}")
else:
    print("CEP não encontrado ou inválido.")