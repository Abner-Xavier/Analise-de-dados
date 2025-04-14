#Primeiros passos: Importar um arquivo e leitura dos dados:
import pandas as pd
Treinamento = pd.read_excel ("EY.xlsx")
print(Treinamento)

#Calcular os lucros:
Total = Treinamento ["Lucro"].sum()
print(Total)

#Faturamento por Loja:
Loja_Faturamento = Treinamento [["Loja", "Lucro"]].groupby("Loja").sum()
print(Loja_Faturamento)

# Agrupar por 'Loja' e 'Satisfação Média'
Loja_Satisfacao = Treinamento[["Loja", "Satisfação Média"]].groupby("Loja").mean()
print(Loja_Satisfacao)

# Agrupar `devolucao`
Loja_Devolutiva = Treinamento[["Loja", "Devoluções"]].groupby("Loja").sum()
print(Loja_Devolutiva)

#Foram calculados seus lucros e clientes satisfeitos, tendo a loja 4 com otimas pontuacoes de Faturamento e Avaliacao acima das demais
#Ao referente a loja 3 tem a melhor venda, tendo baixa devolutiva comparado as demais lojas


