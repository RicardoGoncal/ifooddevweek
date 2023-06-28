# TODO: Implementar a lógica de NPS em comandos simples e sequenciais (imperativo).
import pandas as pd

dados = pd.read_csv('/content/feedbacks.csv', delimiter=';')

detratores = 0
promotores = 0

notas = dados['nota']

for nota in notas:
  if nota >= 9:
    promotores += 1
  elif nota <= 6:
    detratores += 1

nps = (promotores - detratores) / len(notas) * 100
print(nps)



# TODO: Evoluir a implementação para separar melhor as responsabilidades (funcional).
import pandas as pd

def calcular_nps(notas):
  detratores = 0
  promotores = 0

  for nota in notas:
    if nota >= 9:
      promotores += 1
    elif nota <= 6:
      detratores += 1

  nps = (promotores - detratores) / len(notas) * 100
  return nps

dados = pd.read_csv('/content/feedbacks.csv', delimiter=';')

notas = dados['nota']

print(calcular_nps(notas))



# TODO: Abstrair o problema usando classes e objetos (orientação a objetos).
import pandas as pd

class Feedback:
  def __init__(self, nota, comentario):
    self.nota = nota
    self.comentario = comentario

class AnalisadorFeedback:
  def __init__(self, feedbacks):
    self.feedbacks = feedbacks

  def calcular_nps(self):
    detratores = sum([1 for feedback in self.feedbacks if feedback.nota <= 6])
    promotores = sum([1 for feedback in self.feedbacks if feedback.nota >= 9])

    return (promotores - detratores) / len(self.feedbacks) * 100

dados = pd.read_csv('/content/feedbacks.csv', delimiter=';')

feedbacks = [Feedback(linha['nota'], linha['comentario'])  for i, linha in dados.iterrows()]

analisador = AnalisadorFeedback(feedbacks)
nps = analisador.calcular_nps()

print(nps)