import csv
import json
import statistics

def analisar_log_treinamento(nome_arquivo):
 
    try:
        tempos_execucao = []
        
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                
                if 'tempo' in linha.lower() or 'time' in linha.lower():
                    
                    palavras = linha.split()
                    for palavra in palavras:
                        try:
                            
                            numero = float(palavra.replace(',', '.'))
                            tempos_execucao.append(numero)
                        except ValueError:
                            continue
        
        if tempos_execucao:
            media = statistics.mean(tempos_execucao)
            desvio_padrao = statistics.stdev(tempos_execucao) if len(tempos_execucao) > 1 else 0
            
            return media, desvio_padrao, tempos_execucao
        else:
            return None, None, []
            
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return None, None, []
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return None, None, []

print("Criando arquivo de log de exemplo...")
with open('log_treinamento.txt', 'w', encoding='utf-8') as f:
    f.write("Início do treinamento\n")
    f.write("Época 1 - Tempo: 40.5 segundos\n")
    f.write("Época 2 - Tempo: 47.2 segundos\n")
    f.write("Época 3 - Tempo: 54.8 segundos\n")
    f.write("Época 4 - Tempo: 46.1 segundos\n")
    f.write("Época 5 - Tempo: 42.5 segundos\n")
    f.write("Treinamento finalizado\n")

media, desvio, tempos = analisar_log_treinamento('log_treinamento.txt')

if media is not None:
    print(f"\nTempos de execução encontrados: {tempos}")
    print(f"Média do tempo de execução: {media:.2f} segundos")
    print(f"Desvio padrão: {desvio:.2f} segundos")
else:
    print("Não foi possível calcular as estatísticas.")