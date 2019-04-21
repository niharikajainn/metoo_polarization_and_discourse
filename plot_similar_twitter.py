from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import sys


def plot_words(words):
    #loads previously-created word embedding
    model = Word2Vec.load('model_metoo_tweets.bin')
    
    #maps 100-dimensional vectors to 2-dimensions
    pca = PCA(n_components=2)
    transformed = pca.fit_transform([model[word] for word in words])
    
    #plot and label words
    plt.scatter(transformed[:,0], transformed[:,1], color='teal')
    plt.xticks([])
    plt.yticks([])
    for i, word in enumerate(words):
        plt.annotate(word, xy=(transformed[i,0], transformed[i,1]))
        print(word)
    plt.show()

#enter words to plot and type 'exit' when finished
keywords = []
for line in sys.stdin:
    if line.rstrip() != 'exit':
        keywords.append(line.rstrip())
    else:
        plot_words(keywords)
        exit()

