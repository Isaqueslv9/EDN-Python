import json

print("LER E ESCREVER JSON")


def escrever_json(nome_arquivo, dados):
 
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
    except Exception as e:
        print(f"Erro ao escrever arquivo: {e}")

def ler_json(nome_arquivo):

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return None


pessoa_json = {
    'nome': 'Carlos Ferreira',
    'idade': 32,
    'cidade': 'Porto Alegre',
    'profissao': 'Engenheiro',
    'hobbies': ['leitura', 'programação', 'música']
}

print("\nEscrevendo dados em JSON...")
escrever_json('pessoa.json', pessoa_json)

print("\nDados escritos:")
print(json.dumps(pessoa_json, ensure_ascii=False, indent=2))

print("\nLendo dados do JSON...")
dados_json = ler_json('pessoa.json')

if dados_json:
    print("\nDados lidos do arquivo:")
    print(f"Nome: {dados_json['nome']}")
    print(f"Idade: {dados_json['idade']}")
    print(f"Cidade: {dados_json['cidade']}")
    print(f"Profissão: {dados_json['profissao']}")
    print(f"Hobbies: {', '.join(dados_json['hobbies'])}")