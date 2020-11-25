#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sklearn pipelines

Created on Tue Nov  3 16:03:13 2020

@author: David
"""


# load (from) modules
import sys; sys.executable
#from copy import deepcopy
import os
os.chdir("/Users/David/Documents/Studien/2020_ws_bonn/")

import pandas as pd
from pandas import DataFrame
import numpy as np
#import string
#import seaborn as sns; sns.set()

# Pipeline related
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

# Ein sehr kleiner Corpus
str_list = ["Ich liebe NLP. Ich fühle mich dort sehr zuhause. :-)",
"NLP ist doof",
"Machine Learning ist das beste. 1000 mal beser als..."]

# =============================================================================
#  Existierende Transformer
# =============================================================================

# Erstelle Instanz
vect = CountVectorizer(lowercase = False, # Groß oder Kleinschreibung
                       token_pattern='\S+' # Tokenization: alles, was kein whitespace ist/
                       # Einfach ausprobieren. z.B. hier: https://regex101.com/
                       # Default zu präferieren
                       )

# Fitte den Countvectorizer an den Corpus
vect.fit(str_list)
dtm = vect.transform(str_list)
print(dtm)

# Betrachte die Matrix als Dataframe
print(DataFrame(dtm.A, columns=vect.get_feature_names()).to_string()) 

# So wird damit ein neues Dokument transformiert
str_neu = ["Ich liebe NLP auch"]
dtm_neu = vect.transform(str_neu)
print(DataFrame(dtm_neu.A, columns=vect.get_feature_names()).to_string())

# =============================================================================
# Ein prototypischer Transformer, selbst geschrieben
# =============================================================================
class custom_scaler(BaseEstimator, TransformerMixin ):
    # Diese Klasse ist nur eine Vorlage
    # Der Transformer muss erst als Objekt konstruiert werden
    
    def __init__( self, on = True):
        self # Das Objekt selbst
        self.on = on # Wir können dem Objekt eine Eigenschaft zuordnen
    
    # X ist das Feature, y die eventuellen labels
    def fit(self, X, y = None): 
        # Hier "lernt" die pipeline das Maximum von X
        # typischerweise aus den Trainingsdaten
        max_x = max(np.array(X))
        self.max_x = max_x
        return self # Ausgabe ist einfach das instantiierte Objekt selbst
    
    # X ist das Feature, y die eventuellen labels
    def transform(self, X, y = None):
        # Hier wird die Information aus dem fit genutzt
        # d.h. es muss zunächst gefittet worden sein
        # Definiert X0 als X
        X0 = X 
        
        # Hier findet die Skalierung statt
        # Man beachte, dass das Maximum aus dem der fit-Methode stammt
        X = np.array(X)/self.max_x 
        
        # Gebe die Transfomierte nur aus, wenn on == True ist
        if self.on == True:
            return X
        if self.on == False:
            return X0
    
# Zwei Beispiellisten
X1 = [1,2,3,1,2,3]
X2 = [2,3,1,1,1,2]

# Konstruiere aus der Klasse einen "scaler"
scaler_01 = custom_scaler(on = True)

# fitte den scaler an die X1 Daten
scaler_01.fit(X1)

# Transformiere X1
scaler_01.transform(X1)

# Transformiere X2
scaler_01.transform(X2)

# =============================================================================
# Schreibe selbst einen Transformer, der eine Variable aus einem DataFrame 
# extrahiert extrahiert die richtige Variable mit dem Namen var aus einem 
# DataFrame
# =============================================================================

# Häufig befindet sich der Text in einem DataFrame
df = pd.read_csv("data_task2_complete.csv")
df.columns

df["OMT_texts"].values

class ExtractVarTrans(BaseEstimator, TransformerMixin ):
    #Class Constructor 
    def __init__( self, var):
        self
        self.var = var
    def fit(self, X, y = None):
        return self # mache hier sonst nichts
    def transform(self, X, y = None):
        return X[self.var].values # Hier wird die Spalte ausgewählt

ext = ExtractVarTrans(var =  "OMT_texts")
ext.fit(df)
ext.transform(df)
ext.fit_transform(df)

# =============================================================================
# Mögliche Aufgabe: Schreiben Sie selbst einen Transformer, der alle Buchstaben
# in Kleinbuchstaben umwandelt und probieren Sie ihn aus.
# =============================================================================
# Wiederholung:
# # einzelner String
# "HAllo".lower()
# # Als list comprehension
# [X.lower() for X in str_list] 
# =============================================================================
# Lösung im Chat
# 10 Minuten Bearbeitung
# 5 Minuten Besprechung
# =============================================================================
# =============================================================================
