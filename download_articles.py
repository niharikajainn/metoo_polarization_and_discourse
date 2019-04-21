from newspaper import Article
from gensim.models import Word2Vec
import time
import urllib
import pickle
import string
from collections import defaultdict

websites = []
with open ("links_metoo.txt", "rb") as f:
    websites = pickle.load(f)
f.close()


documents = []
count_article = 0
for url in websites:
    count_article += 1
    print("Article " + str(count_article))
    started = time.time()
    article = Article(url.strip(), request_timeout=50)
    article.download()
    article.parse()
    text = article.text
    documents.append(text)
    ended = time.time()
    print("Processed in " + str(ended-started) + " seconds.")


stopwords = set([ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ])

translator = str.maketrans('', '', string.punctuation)
documents = [document.translate(translator) for document in documents]
documents = [[word.lower() for word in document.split() if word not in stopwords] for document in documents]

with open("documents_metoo.txt", "wb") as f:
    pickle.dump(documents, f)

model = Word2Vec(documents, min_count=2)
model.save('model_metoo.bin')


