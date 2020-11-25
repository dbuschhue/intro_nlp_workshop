#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pipelines, Classification

Created on Tue Nov  3 16:03:13 2020

@author: David
"""

# =============================================================================
# =============================================================================
# TEIL A
# =============================================================================
# =============================================================================

# Laden von Modulen
import os

# Schreibe Pfad
path = "/Users/David/Documents/Studien/2020_ws_bonn"
os.chdir(path)
out_path = path+"/output"

import sys; sys.executable
import pandas as pd
import numpy as np
import sklearn

import sys; sys.executable
import pickle
from datetime import datetime
import seaborn as sns; sns.set()

# Pipeline 
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# Modellauswahl
from sklearn.model_selection import cross_validate, \
    RandomizedSearchCV, GridSearchCV, ParameterGrid
from sklearn.metrics import classification_report
    

# Classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier

# =============================================================================
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import f1_score
# from sklearn.ensemble import VotingClassifier
# from sklearn.neighbors import KNeighborsClassifier
# import string
# from make_scorer, confusion_matrix
# =============================================================================

# Transformer, der eine Variable extrahiert
class ExtractVarTrans(BaseEstimator, TransformerMixin ):
    #Class Constructor 
    def __init__( self, var):
        self
        self.var = var
    def fit(self, X, y = None):
        return self
    def transform(self, X, y = None):
        return X[self.var].values
    

# =============================================================================
# Daten laden
# =============================================================================
df_train = pd.read_csv("df_train.csv")
df_train.columns

labels_train = df_train["motive"]

# Reduziere Anzahl Fälle in Trainingsdaten aus Zeitgründen für den Workshop
df_train_red = df_train.iloc[0:3000]
labels_train_red = labels_train.iloc[0:3000]

# Stopwords aus NLTK laden
mystopwords = stopwords.words("german")

# =============================================================================
# Konstruktion einer Pipeline
# =============================================================================

# Konstruiere Pipeline aus sogenannten tupeln
pipe_text =  Pipeline([
    ("extract text", ExtractVarTrans(var = "OMT_texts")),
    # transformiert in Doc-Term-Matrix
    ("CountVec", CountVectorizer(min_df = 0, 
                                 max_df = 150, #entferne eher unbedeutende Begriffe
                                 stop_words = mystopwords)),
    ("tfidf", TfidfTransformer())]
    )

# Fitten der Pipeline
pipe_text.fit(df_train_red)

# Transformieren
out = pipe_text.transform(df_train_red)

# =============================================================================
# Erweiterung um Klassifikation
# =============================================================================

# Füge zu vorhandenen Pipeline logistische Regression hinzu
pipe_lr = Pipeline([("pipe_text", pipe_text),
                      ("logreg",LogisticRegression(max_iter = 1000))])

# Speichere default parameters für später
default_lr_params = pipe_lr.get_params()

# Fitte gesamte Pipeline
pipe_lr.fit(df_train_red, df_train_red["motive"])

# Speichere
now = datetime.now()
pickle.dump(pipe_lr,open( out_path+"/"+
                         now.strftime("%d_%m_%Y_%H_%M")+"_log_reg"+".p","wb" ))
# Wenn ein Modell geladen werden soll:
# pipe_lr = pickle.load( open( out_path+"/"+"DATEINAME.p" , "rb") )
y_pred_lr = pipe_lr.predict(df_train_red)
cr = classification_report(labels_train_red, y_pred_lr, output_dict = False)
print(cr)

# =============================================================================
# =============================================================================
# TEIL B
# =============================================================================
# =============================================================================

# =============================================================================
# Kreuzvalidierung
# =============================================================================

# Probiere unterschiedliche Modelle aus
# Classifier
classifiers = [
    DecisionTreeClassifier(random_state = 42),
    MultinomialNB(),
    SVC(),
    LogisticRegression(),
    RandomForestClassifier(random_state = 42)
    ]


# Classfier Namen
names = [
    "Decision Tree",
    "Multinomial Naive Bayes",
    "Support Vector Classifier",
    "Logistic Regression",
    "Random Forest"]

scores_cvo = pd.DataFrame(columns = ["Classifier", "Score", "Metric"])
k = 3

# Ausgewählte Qualitätsmaße
metric_list = ["accuracy","f1_macro"]

# Schleife über die Classifier
for name, clf in zip(names, classifiers):
    
    # Integriere den Classifier
    full_pipe = Pipeline([("pipe_text", pipe_text),  ("clf",clf)])
    
    # Eigentliche Kreuzvalidierung
    score_x = cross_validate(full_pipe, df_train_red, labels_train_red, 
                             scoring = metric_list , cv = k, n_jobs = -1)

    scores_clasif_x = pd.DataFrame(columns = ["Classifier", "Score", "Metric"])
    
    # Schreibe Werte des Outputs in ein Dataframe
    # Mache das für alle ausgewählten Qualitätsmaße
    for metric_x in metric_list:
        df_score = pd.DataFrame(
            {'Classifier': [name]*k, 
             'Score': score_x["test_"+metric_x].tolist(),
             'Metric': [metric_x]*k}, 
            columns=['Classifier','Score', "Metric"])
        # HÄnge die Ausgabe zu dieser Metrik and das Dataframe an
        scores_clasif_x = scores_clasif_x.append(df_score)
    # Hänge die Ausgaben aller Metriken an dieses Dataframe an
    scores_cvo = scores_cvo.append(scores_clasif_x)

    print(name)
   # print(conf_mat)
   
# Ausgabe als Plot
ax = sns.pointplot(y="Classifier", x="Score", data=scores_cvo, join=False, 
                   hue="Metric")

# =============================================================================
# Hyperparameter Tuning
# =============================================================================

# Anzahl folds für Kreuzvalidierung während des Tunings
k_tune = 3

# =============================================================================
# Hyperparameter-Tuning: Hier nur für logistische Regression
# =============================================================================

# Anzahl Kandidaten für Parametereinstellungen
n_iter_rand = 50

# Zahlen in gleichmäßigen Abständen auf einer Log-Skala
C_vals = np.logspace(-4, 4, 20) 

# 
grid_rs_list_lr = [{
  'pipe_text__CountVec__min_df': [2,3,4,5],
  'pipe_text__CountVec__max_df': [10,50,80,90,150,200],
  'logreg__penalty' : ['elasticnet'],
  'logreg__l1_ratio': [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
  'logreg__C' : C_vals,
  'logreg__solver' : ['saga'], # so we can use elastic net
  'logreg__random_state': [42],
  'logreg__max_iter' : [10000]}]

# Wie viele Einstellungen hat das Grid
len(list(ParameterGrid(grid_rs_list_lr)))

# random search cross validation
random_s_lr = RandomizedSearchCV(estimator = pipe_lr, # Modellspezifikation
                                 param_distributions = grid_rs_list_lr  , # Hyperparameter
                                 n_iter = n_iter_rand, # Anzahl Kombinationen
                                 cv = k_tune, # Folds
                                 verbose=2, # Output während des Rechnens
                                 random_state=42, # Reproduzierbarkeit
                                 scoring = "accuracy", # welches Merkmal soll maximiert werden?
                                 n_jobs = -2) #  (Anzahl verwendete CPUS = n_cpus + 1 + n_jobs) werden 
# Fitte
random_s_lr.fit(df_train_red, labels_train_red)

# Speichere 
now = datetime.now()
pickle.dump(random_s_lr,
            open( out_path+"/"+
                 now.strftime("%d_%m_%Y_%H_%M")+"_random_s_lr"+".p","wb" ))
# Wenn ein Modell geladen werden soll:
# pipe_lr = pickle.load( open( out_path+"/"+"DATEINAME.p" , "rb") )

# Ergebnisse
print("Best Score: ", random_s_lr.best_score_)
print("Best Parameters: ", random_s_lr.best_params_)

# =============================================================================
#  Grid Search
# =============================================================================
grid_s_list_lr =  [{'pipe_text__CountVec__min_df': [2,3,4],
 'pipe_text__CountVec__max_df': [190,200, 210],
 'logreg__solver': ['saga'],
 'logreg__l1_ratio': [0.2,0.3,0.35],
 'logreg__penalty': ['elasticnet'],
 'logreg__max_iter': [10000],
 'logreg__C': [0.7, 1, 1.623776739188721, 2,3,4],
   }]

np.logspace(-1,1,10)

# Wie viele Einstellungen hat das Grid
len(list(ParameterGrid(grid_s_list_lr)))

# Grid Search
grid_s_lr = GridSearchCV(pipe_lr, grid_s_list_lr, scoring = "accuracy",
                                 verbose = 2, 
                                cv = k_tune, n_jobs = -2)

grid_s_lr.fit(df_train_red, labels_train_red)

print("Best Score: ", grid_s_lr.best_score_)
print("Best Parameters: ", grid_s_lr.best_params_)

# Speichere
now = datetime.now()
pickle.dump(grid_s_lr,
            open( out_path+"/"+now.strftime("%d_%m_%Y_%H_%M")+"_grid_s_lr"+".p"
                 ,"wb" ))

# Wenn ein Modell geladen werden soll:
# grid_s_lr = pickle.load( open( out_path+"/"+"DATEINAME.p" , "rb") )


# =============================================================================
#  Vergleiche mit Modell mit Default Einstellungen
# =============================================================================

# Übergebe die default Parameter als dictionairy mit ** (kwarg)
pipe_lr.set_params(**default_lr_params)
# Kreuzvalidierung
score_x = cross_validate(pipe_lr, df_train_red, labels_train_red, 
                             scoring = "accuracy" , cv = 10, n_jobs = -1)
print(score_x['test_score'].mean())

# Übergebe die besten Parameter als dictionairy
pipe_lr.set_params(**grid_s_lr.best_params_)
# Kreuzvalidierung
score_x= cross_validate(pipe_lr, df_train_red, labels_train_red, 
                             scoring = "accuracy" , cv = 10, n_jobs = -1)
print(score_x['test_score'].mean())

# =============================================================================
#  Wende das bessere Modell auf den Test-Datensatz an
# =============================================================================

# Übergebe die besten Parameter als dictionairy mit ** (kwarg)
pipe_lr.set_params(**grid_s_lr.best_params_)
pipe_lr.fit(df_train_red, df_train_red["motive"])

# Speichere Modell ab
now = datetime.now()
pickle.dump(pipe_lr,open( 
    out_path+"/"+now.strftime("%d_%m_%Y_%H_%M")+"_pipe_lr_best"+".p",
    "wb" ))

# Wenn ein Modell geladen werden soll:
# pipe_lr = pickle.load( open( out_path+"/"+"DATEINAME.p" , "rb") )

# Lade Testdaten
df_test = pd.read_csv("df_test.csv")

# Definiere Labels
labels_test = df_test["motive"]

# Mache Vorhersage
y_test_pred = pipe_lr.predict(df_test)

# Schreibe Bericht
print(classification_report(labels_test, y_test_pred))
y_test_pred = pipe_lr.predict(df_test)


