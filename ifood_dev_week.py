import pandas as pd

class Feedback():
    def __init__(self, nota, comentario):
        
        self.nota = nota
        self.comentario = comentario


class AnalisadorFeedback():
    def __init__(self, feedbacks):
        self.feeds = feedbacks


    def calcular_nps(self):

        # variaveis
        promotores = sum(1 for feedback in self.feeds if feedback.nota >= 9)
        detratores = sum(1 for feedback in self.feeds if feedback.nota <= 6)

        # Calculo de NPS
        nps = (promotores - detratores) / len(self.feeds) * 100

        return nps


if __name__ == '__main__':

    # Exportar Dados
    dados = pd.read_csv('./feedbacks.csv',sep=";")
    # print(dados)

    # Faz uma lista de objetos com as infos de feedback
    feedbacks = [ Feedback(linha['nota'], linha['comentario']) for indice, linha in dados.iterrows()]
    # print(feedbacks)

    # Instancia a classe de analise e chama o metodo de calculo de nps
    analise_feed = AnalisadorFeedback(feedbacks)
    nps = analise_feed.calcular_nps()

    print(nps)
    