def media(base):
    soma = 0
    for i in base:
        soma += i
    var = soma / len(base)
    return var

def mediana(base):
  
    if len(base) % 2 == 0:
      return (base[len(base) // 2 - 1]) + (base[len(base) // 2]) // 2
    else:
      return base[len(base) // 2]
      
def variancia_amostral(base):
    soma = 0
    for i in base:
        soma += (i - media(base)) ** 2
    return soma / (len(base) - 1)
  
def variancia_populacional(base):
  soma = 0
  for i in base:
        soma += (i - media(base)) ** 2
  return soma / len(base) 

def desvio_padrao_amostral(base):
    return variancia_amostral(base) ** 0.5

def desvio_padrao_populacional(base):
  return variancia_populacional(base) ** 0.5

def coeficiente_variacao_amostral(base):
  return desvio_padrao_amostral(base) / media(base) * 100

def coeficiente_variacao_populacional(base):
  return desvio_padrao_populacional(base) / media(base) * 100
  
def quartis(base):
  M = mediana(base)
  q1 = mediana(base[0 : base.index(M)])
  q3 = mediana(base[base.index(M):len(base) - 1])

  return q1, M, q3