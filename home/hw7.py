import gensim
import urllib.request
import os
import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

#качаю модель на материале НКРЯ (2018)
def model_w2v(url):
    m = url.split('/')[-1]
    urllib.request.urlretrieve(url, m)
    if m.endswith('.vec.gz'):
        model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=False)
    elif m.endswith('.bin.gz'):
        model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=True)
    else:
        model = gensim.models.KeyedVectors.load(m)
    return model

#сосавляю семантическое поле
def semfield(words):  
    for word in words:
        for i in model.most_similar(positive=[word], topn=10):
            if i[0] not in field and model.similarity(word, i[0]) >= 0.5:
                field.append(i[0])

#рисую граф, проверяя каждого потенциального соседа по косинусной близости
def draw_gr(words): 
    G = nx.Graph()
    G.add_nodes_from(words, labels=[word[:-5] for word in words])
    for i, word in enumerate(words):
        for pair in words[i+1:]:
            s = model.similarity(word, pair)
            if s >= 0.5:
                G.add_edge(word, pair, weight=s)
    return G

#считаю метрики
def metr_gr(graph):
    deg = nx.degree_centrality(graph)
    max_deg = sorted(deg, key=deg.get, reverse=True)
    print('Max degree centrality:', ", ".join(max_deg[:5]))
    
    bet = nx.betweenness_centrality(graph)
    max_bet = sorted(bet, key=bet.get, reverse=True)
    print('Max betweenness centrality:', ", ".join(max_bet[:5]))

    clos = nx.closeness_centrality(graph)
    max_clos = sorted(clos, key=clos.get, reverse=True)
    print('Max closeness centrality:', ", ".join(max_clos[:5]))
    
    eig = nx.eigenvector_centrality(graph)
    max_eig = sorted(eig, key=eig.get, reverse=True)
    print('Max eigencentrality:', ", ".join(max_eig[:5]))
    
    print('Плотность:', nx.density(graph))
    print('Радиус:', nx.radius(graph))
    print('Диаметр:', nx.diameter(graph))
    print('Коэффициент кластеризации:', nx.average_clustering(graph))
    print('Коэффициент ассортативности:', nx.degree_pearson_correlation_coefficient(graph)) 
    
    return clos

#вывожу граф на экран
def show_gr(graph, metric):          
    pos=nx.spring_layout(graph)        
    nx.draw_networkx_edges(graph, pos, edge_color='grey')
    nx.draw_networkx_labels(graph, pos, font_size=15, font_family='Times New Roman')
    for word in graph.nodes():
        size = metric[word] * 100
        nx.draw_networkx_nodes(graph, pos, nodes=[word], node_color='green', node_size=size) 
    plt.axis('off')
    plt.show()


url = "https://rusvectores.org/static/models/rusvectores4/RNC/ruscorpora_upos_skipgram_300_5_2018.vec.gz"
model = model_w2v(url)
words = ("радио", "телевизор")
field = list(words)
semfield(words) 
grap = draw_gr(field)
metr = metr_gr(grap)
show_gr(grap, metr)
