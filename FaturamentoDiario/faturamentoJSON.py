import json 

def processar_faturamento(filename):
    with open(filename, 'r') as file:
        dados = json.load(file)
    
    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
    
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    
    dias_acima_da_media = len([v for v in valores if v > media_mensal])

    print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
    print(f"Média de faturamento: R$ {media_mensal:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

processar_faturamento('C:/Users/lilgu/Documents/Python_Project/Teste-Target/FaturamentoDiario/dados.json')
