import pandas as pd
import matplotlib.pyplot as plt

def grafico_bacen (code, type, titulo, exp_valor):
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(code)
    dado = pd.read_json(url)

    x = dado['data'][-25:]
    y = dado['valor'][-25:]
    plt.style.use('ggplot')

    if type == 'linear':
        plt.plot(x, y, color='teal', linewidth=2)
    elif type == 'barras':
        plt.bar(x, y, color='teal')
    else: plt.scatter(x, y, color='teal', edgecolors='black')
    
    plt.ylabel('Valor expresso em {}'.format(exp_valor), size=11)
    plt.title(titulo)
    plt.xticks(x, x, rotation='vertical')
    plt.tick_params(labelsize=10)
    plt.show()


grafico_bacen (7326, 'DISPERSAO', 'PIB - Taxa variação real')

