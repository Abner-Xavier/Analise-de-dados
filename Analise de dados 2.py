#Segundo objetivo para treinamento do Pandas

import pandas as pd
Vendas= pd.read_excel("TechNova.xlsx")
print(Vendas)

Lucro_por_produto = Vendas [["Produto", "Lucro"]].groupby("Produto").sum().sort_values(by="Lucro", ascending=False)
print(Lucro_por_produto)
#Os produtos que tem maior numero de venda sao os Fones, Headset e Teclados Slim

Vendas_Quantidade = Vendas [["Loja", "Vendas"]].groupby("Loja").sum().sort_values(by="Vendas", ascending=False)
print(Vendas_Quantidade)
#Lojas Sul e Oeste possuem maiores duas maiores vendas

Devolutivas = Vendas [["Produto", "Devoluções"]].groupby("Produto").sum().sort_values(by="Devoluções", ascending=False)
print(Devolutivas)
#Luminaria Lede Wi-fi, Headset Gamer e Smartwatch Pro possuem maiores devolutivas durantes os ultimos anos analisados

Sazonalidade= Vendas [["Mês", "Vendas" ]].groupby("Mês").sum().sort_values(by="Vendas", ascending=False)
print(Sazonalidade)
# Meses de Abril, Julho e Outubro obtiveram melhores resultados

Clientes_satisfeitos = Vendas [["Loja", "Satisfação Média"]].groupby("Loja").mean().sort_values(by="Satisfação Média", ascending=False)
print(Clientes_satisfeitos)
#Lojas Leste e Sul foram os melhores resultados de satisfacao

Equilibrio = Vendas[["Produto", "Satisfação Média", "Lucro"]].groupby("Produto").mean().sort_values(by=["Lucro", "Satisfação Média"], ascending=False)
print(Equilibrio)
#Os produtos Fone, Headset e Teclado Slim foram os que tiveram melhores demandas e equilibrio nas lojas