import requests
print("CONSULTA DE COTAÇÃO DE MOEDA")


def consultar_cotacao(codigo_moeda):
  
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            chave = f"{codigo_moeda}BRL"
            
            if chave in dados:
                return dados[chave]
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"Erro ao consultar cotação: {e}")
        return None

codigo_moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
cotacao = consultar_cotacao(codigo_moeda)

if cotacao:
    print(f"\nMoeda: {cotacao['name']}")
    print(f"Valor atual: R$ {float(cotacao['bid']):.4f}")
    print(f"Valor máximo: R$ {float(cotacao['high']):.4f}")
    print(f"Valor mínimo: R$ {float(cotacao['low']):.4f}")
    print(f"Data/Hora da atualização: {cotacao['create_date']}")
else:
    print("Moeda não encontrada ou código inválido.")
