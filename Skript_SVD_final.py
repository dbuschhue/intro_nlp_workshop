# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 16:34:51 2020

@author: Peter

### Skript Latent Semantic Analysis

LSA: https://towardsdatascience.com/latent-semantic-analysis-intuition-math-implementation-a194aff870f8
LDA siehe: https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0
"""

import os
import pickle

import matplotlib.pyplot as plt
import matplotlib.gridspec as grd
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

from sklearn.decomposition import TruncatedSVD
from scipy.sparse import random as sparse_random
from sklearn.random_projection import sparse_random_matrix

from nltk.corpus import stopwords
german_stopwords = stopwords.words('german')

# change this path to your working tree:
os.chdir('C:/Users/Peter/Documents/presentations/workshop_NLP_11-2020/analyses')

### Load the data that has been used in the first part of the workshops as well:
# Needs to point to the data dir: '..' gets you to the parent dir
# you can see the current dir with 'os.getwd()'
train = pd.read_csv( '../data/df_train.csv' )
test = pd.read_csv( '../data/df_test.csv' )

X_train = train.OMT_texts
y_train = train.motive
X_test = test.OMT_texts
y_test = test.motive

# perform some preprocessing with the documents (here you can enter preprocessing as you like):
# you can play with parameters max_df (maximum number of a term in vocab) and min_df
tfidf = TfidfVectorizer(lowercase=True, max_df=1.0, min_df=1, stop_words = german_stopwords )
X_train_tfidf = tfidf.fit_transform( X_train )
X_test_tfidf = tfidf.transform( X_test )


# now we perform SVD to reduce data dimensionality:
svd = TruncatedSVD( n_components=20, random_state = 42 )
svd.fit( X_train_tfidf )
fitted_svd = svd.transform( X_train_tfidf )

# importance of topics: dargestellt als einfacher lineplot
s = svd.singular_values_
plt.plot(s)

# get the associations of terms with concepts in the Term-Concept-Matrix:
V_T = svd.components_.T 
term_topic_matrix = pd.DataFrame(data=V_T, 
                                 index = tfidf.get_feature_names(), 
                                 columns = [f'Latent_concept_{r}' for r in range(0,V_T.shape[1])]) 

# print top 10 words for top 10 concepts:
for i in range(20):
    data = term_topic_matrix[f'Latent_concept_' + str(i)]
    data = data.sort_values(ascending=False)
    top_10_str = ', '.join([ token for token in data[:10].index ])
    print( 'Top 10 words for latent concept {}: {}'.format( str(i),top_10_str ) )

    # print out top 10 words in barplot:
    plt.title('Top terms along the axis of Latent concept 1')
    fig = sns.barplot(x= data[:10].values, y=data[:10].index)
    plt.show(fig)


## How many dimensions are good enough to capture the variance in the data?
## Now, the goal is to find a minimal set of dimensions, that captures data equally well as full dataset:
# We do this by fitting logistic regressions based on the labels (y_train)

# First we fit a baseline model that captures the performance for the entire dataset
# These are some hyperparameters that control the fit algorithm. Details don't matter much
logreg_param_grid = [{'penalty':['l1', 'l2']},
                     {'tol':[0.0001, 0.0005, 0.001]}]

# you know this object from classification in part I of the workshop:
logreg = LogisticRegression(max_iter = 10000)
# here is an additional feat to optimize the hyperparameters of the fitting algorithm:
grid_log = GridSearchCV(estimator=logreg,
                        param_grid=logreg_param_grid, 
                        scoring='f1_weighted', cv=5,
                        n_jobs=-1)

# the next command will take a while:
best_reg_logreg = grid_log.fit(X_train_tfidf, y_train).best_estimator_

# now the loop over different values for the dimension in svd. We check, when the performance with reduced dimension
# approximates the performance with the full dataset (see print commands in ll 106-109)
# Note: the loop might take some time, because it is computationally involved
# you can adjust the start, stop, step parameters to your demands
for dims in np.arange(start=5,stop=400,step=100):
    # fit the svd to the data
    lsa_obj = TruncatedSVD(n_components=dims, n_iter=7, random_state=42)
    # fit SVD on training data with specified dims in order to get reduced matrices to transform test data
    X_train_tfidf_lsa = lsa_obj.fit_transform(X_train_tfidf)
    X_test_tfidf_lsa = lsa_obj.transform(X_test_tfidf)

    # output feature names for later use:
    V_T = lsa_obj.components_.T    
    term_topic_matrix = pd.DataFrame(data=V_T, 
                                     index = tfidf.get_feature_names(), 
                                     columns = [f'Latent_concept_{r}' for r in range(0,V_T.shape[1])]) 
    
    # create two objects for LogReg, one with LSA-reduced data, one without
    # This is in order to check when LSA-reduced data approximates performance of data without LSA-reduction
    logreg_lsa = LogisticRegression(max_iter = 10000)
    
    # fit the data with LogReg objects; with 5-fold crossvalidation, accuracy as score,
    grid_lsa_log = GridSearchCV(estimator=logreg_lsa,
                            param_grid=logreg_param_grid, 
                            scoring='accuracy', cv=5,
                            n_jobs=-1)
    best_lsa_logreg = grid_lsa_log.fit(X_train_tfidf_lsa, y_train).best_estimator_
    
    print( 'Number of components: {}'.format(dims) )
    print("F1 weighted of Logistic Regression on LSA train data is :", best_lsa_logreg.score(X_train_tfidf_lsa, y_train))
    print("F1 weighted of Logistic Regression with standard train data is :", best_reg_logreg.score(X_train_tfidf, y_train))
    print('\n')


# now the moment of truth: does it perform equally well on the test data?
y_pred_lsa = grid_lsa_log.predict(X_test_tfidf_lsa)
print( classification_report(y_test, y_pred_lsa) )

y_pred = grid_log.predict(X_test_tfidf)
print( classification_report(y_test, y_pred) )


# Now lets see if the svd splitted the documents according to their labels - or if there is no relation (note that this is just 
# a first glimpse - much further analyses have to be performed in order to validate these findings)
# plot 2-dimensional mapping of svd:
colors = {'A': 'red', '0': 'grey', 'F': 'green', 'L': 'blue', 'M': 'orange'}
# redering the following plot will also use many resources on your machine
plt.scatter(X_train_tfidf_lsa[:,3], # this is parameter for x-axis
            X_train_tfidf_lsa[:,4], # y-axis
            c=y_train.map(colors) # color indicator
            )


### predict a new, unseen sample:
# you can adjust the sentence as you like and see if sth reasonable comes out!
sample = ['Er erreicht das Ziel auf dem Berg']
sample_tfidf = tfidf.transform(sample)

concept = np.argmax( lsa_obj.transform(sample_tfidf) )
print( 'concept {} is the closest.'.format(concept) )

top_10_words_indices = np.argsort( term_topic_matrix[f'Latent_concept_' + str(concept)] )[-10:]
words = [ term_topic_matrix.index[n] for n in top_10_words_indices ]
print( 'This concept is characterized by the top 10 words: {}'.format(words) )


# retrieve similar documents in the corpus:
closest_docs_values = X_train_tfidf_lsa@lsa_obj.transform(sample_tfidf).T
indices = np.argsort( closest_docs_values.reshape(-1,) )[-10:]
closest_docs = '\n\n '.join( [ doc for doc in X_train[ indices ] ] )
print( 'These are the closed docs: \n {}'.format(closest_docs) )
