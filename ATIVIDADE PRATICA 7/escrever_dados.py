import csv

print("ESCREVER DADOS EM CSV")

def escrever_csv(nome_arquivo, dados):
    
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
            if dados:
               
                colunas = dados[0].keys()
                escritor = csv.DictWriter(arquivo, fieldnames=colunas)
                
                
                escritor.writeheader()
                
                
                escritor.writerows(dados)
                
                print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
    except Exception as e:
        print(f"Erro ao escrever arquivo: {e}")


dados_pessoas = [
    {'Nome': 'João Silva', 'Idade': 30, 'Cidade': 'São Paulo'},
    {'Nome': 'Maria Santos', 'Idade': 25, 'Cidade': 'Rio de Janeiro'},
    {'Nome': 'Pedro Oliveira', 'Idade': 35, 'Cidade': 'Belo Horizonte'},
    {'Nome': 'Ana Costa', 'Idade': 28, 'Cidade': 'Curitiba'}
]

escrever_csv('pessoas.csv', dados_pessoas)
print("Dados escritos:")
for pessoa in dados_pessoas:
    print(f"  {pessoa['Nome']} - {pessoa['Idade']} anos - {pessoa['Cidade']}")