from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import sys
import re


def most_similar(to, num):
    model = Word2Vec.load('model_metoo_tweets.bin')
    word_vectors = model.wv
    similar = []
    similar += [word[0] for word in word_vectors.most_similar(to, topn=num)]
    print(similar)

for line in sys.stdin:
    if line.rstrip() != 'exit':
        try:
            #print the three most similar words for input
            most_similar(line.rstrip(), 3)
        except:
            #word does not exist in corpus
             print('[]')
    else:
        exit()


