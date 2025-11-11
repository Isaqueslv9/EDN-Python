import csv

print("LER DADOS DE CSV")

def ler_csv(nome_arquivo):
  
    try:
        dados = []
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            
            print(f"\nLendo arquivo '{nome_arquivo}':\n")
            print(f"{'Nome':<20} {'Idade':<10} {'Cidade':<20}")
            print("-" * 50)
            
            for linha in leitor:
                dados.append(linha)
                print(f"{linha['Nome']:<20} {linha['Idade']:<10} {linha['Cidade']:<20}")
        
        return dados
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return []

dados_lidos = ler_csv('pessoas.csv')
print(f"\nTotal de registros lidos: {len(dados_lidos)}")