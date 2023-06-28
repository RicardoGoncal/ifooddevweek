import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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



def criar_grafico_nps(nps):

    # Cria figura e armazena os eixos em ax
    fig, ax = plt.subplots(figsize=(10,2))

    # iteração para criar grafico de barras
    for i, zona in enumerate(NPS_ZONAS):
        ax.barh([0],width=NPS_VALORES[i+1]-NPS_VALORES[i], left=NPS_VALORES[i], color=NPS_CORES[i])

    # Trabalho em cima do objeto plot para ajusta-lo
    ax.barh([0], width=0.5, left=nps) # Faz uma pequena barra na localidade do nps para indicar posição
    ax.set_yticks([]) # Tira os valores de Y no grafico
    ax.set_xlim(-100,100) # Ajusta tamanho da regua(escala)
    ax.set_xticks(NPS_VALORES) # Ajusta valores do X 

    plt.title("Analise de NPS", loc='center') # Acrescenta Titulo
    plt.text(nps,0,f'{nps:.2f}', ha='center', va='center', color='white', bbox=dict(facecolor='black')) # Acrescenta texto na posicao nps
    
    patches = [mpatches.Patch(color=NPS_CORES[i], label=NPS_ZONAS[i]) for i in range(len(NPS_ZONAS))] # Cria um pacote de legendas
    plt.legend(handles=patches, bbox_to_anchor=(1,1)) # Atribui as legendas

    plt.show() # Exibe o grafico



if __name__ == '__main__':

    # Exportar Dados
    dados = pd.read_csv('./feedbacks.csv',sep=";")
    # print(dados)

    # Faz uma lista de objetos com as infos de feedback
    feedbacks = [Feedback(linha['nota'], linha['comentario']) for indice, linha in dados.iterrows()]
    # print(feedbacks)

    # Instancia a classe de analise e chama o metodo de calculo de nps
    analise_feed = AnalisadorFeedback(feedbacks)
    nps = analise_feed.calcular_nps()

    # Definição das constantes para visualizar o NPS
    NPS_ZONAS = ['Critico','Aperçoamento','Qualidade','Excelencia']
    NPS_VALORES = [-100,0,50,75,100]
    NPS_CORES = ['#FF595E','#FFCA3A','#8AC926','#1982C4']

    # Criar gráfico com matplotlib para o NPS
    criar_grafico_nps(nps)