from matplotlib.pyplot import *
from funcoes import *
from statistics import *

dados = [78, 46, 37, 26, 10, 10, 54, 82, 66, 42, 24, 4, 34, 83, 71 ]
dados.sort()

print("|=|=|=|- Base de Dados 2 -|=|=|=|")
print("\n-Dados:", dados)
print("-Número de elementos:", len(dados))
print("")

print("|=|=|=|- Média -|=|=|=|")
print(f"\n- Funções do Estudante: {media(dados): .2f}")
print(f"\n- Funções do Python: {mean(dados): .2f}")
print("")

print("|=|=|=|- Mediana -|=|=|=|")
print(f"\n- Funções do Estudante: {mediana(dados): .2f}")
print(f"\n- Funções do Python: {median(dados): .2f}")
print("")

print("|=|=|=|- Variância -|=|=|=|")
print(f"\n- Funções do Estudante:")
print(f"  > Variância Amostral: {variancia_amostral(dados): .2f}")
print(f"  > Variância Populacional: {variancia_populacional(dados): .2f}")
print(f"\n- Funções do Python:")
print(f"  > Variância Amostral: {variance(dados): .2f}")
print(f"  > Variância Populacional: {pvariance(dados): .2f} ")
print("")

print("|=|=|=|- Desvio Padrão -|=|=|=|")
print(f"\n- Funções do Estudante:")
print(f"  > Desvio Padrão Amostral: {desvio_padrao_amostral(dados): .2f}")
print(f"  > Desvio Padrão Populacional: {desvio_padrao_populacional(dados): .2f}")
print(f"\n- Funções do Python: ")
print(f"  > Desvio Padrão Amostral: {stdev(dados): .2f}")
print(f"  > Desvio Padrão Populacional: {pstdev(dados): .2f}")
print("")

print("|=|=|=|- Coeficiente de Variação -|=|=|=|")
print(f"\n- Funções do Estudante:")
print(f"  > Coeficiente de Variação Amostral: {coeficiente_variacao_amostral(dados): .2f} %")
print(f"  > Coeficiente de Variação Populacional: {coeficiente_variacao_populacional(dados): .2f} %")
print(f"\n- Funções do Python: ")
print(f"  > Coeficiente de Variação Amostral: {stdev(dados) / mean(dados) * 100: .2f} %")
print(f"  > Coeficiente de Variação Populacional: {pstdev(dados) / mean(dados) * 100: .2f} %")
print("")

print("|=|=|=|- Quartis -|=|=|=|")
q1,M, q3 = quartis(dados)
quartisModulo = quantiles(dados, n = 4)

print(f"\n- Funções do Estudante:")
print(f"  > Primeiro Quartil:{q1}")
print(f"  > Terceiro Quartil: {q3}")
print(f"\nFunções do Python:")
print(f"  > Primeiro Quartil:{quartisModulo[0]}")
print(f"  > Terceiro Quartil: {quartisModulo[2]}")
print("")

print("|=|=|=|- Box Plot -|=|=|=|")
boxplot(dados)
title("Box Plot com base de dados criaca", loc = "center", fontsize = 15)
ylabel("Valores dos dados")
show()

