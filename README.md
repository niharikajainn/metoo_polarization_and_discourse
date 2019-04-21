# metoo_polarization_and_discourse
Creates and analyzes two custom corpora discussing the #MeToo movement

From an online library resource which allows it, use code structured similarly to collect_article_links.py and download_articles.py to automate collection of news articles matching a search query. This code also creates a word embedding model_metoo_wsj.bin for the corpus using Gensim's Word2Vec library.

Collect tweets using Twitter Developer's API endpoints for search with code structured similarly to collect_tweets.py. My corpus of tweets is stored in tweets_metoo.txt. This also creates a word embedding model_metoo_twitter.bin.

Analyze the word embedding given a .bin file containing the Gensim model with similarity_twitter.py, cosine_distances_twitter.py, and plot_similar.py. 

