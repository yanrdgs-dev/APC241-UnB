# Questão 1
dolar = float(input())
tamanhoLote = int(input())
totalLotes = int(input())
precoLote = (dolar * tamanhoLote)
taxaLote = precoLote * 0.025

for i in range(totalLotes):
    print(f"Lote: {i + 1} - Total da venda: R$ {precoLote + taxaLote:.2f}")