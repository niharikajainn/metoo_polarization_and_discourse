from gensim.models import Word2Vec
import sys
import re


def print_cosine_distance(word1, word2):
    model = Word2Vec.load('model_metoo_tweets.bin')
    print(model.similarity(word1, word2))

for line in sys.stdin:
    if line.rstrip() == 'exit':
        exit()
    try:
        #takes two comma-separated words as input
        word1, word2 = re.split(', ', line)
        word2 = word2.rstrip()
        #print cosine distance if both exist in corpus
        print_cosine_distance(word1, word2)
    except:
        #at least one word not in corpus or invalid input
        print('[]')
