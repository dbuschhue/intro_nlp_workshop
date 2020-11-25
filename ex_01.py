#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Einfache Textvorverarbeitung

Created on Tue Nov  3 13:51:44 2020

@author: David Buschhüter, Peter Wulff
"""

# Importiere aus Modulen
import string
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

# Das ist eine Beispiel-Liste mit Strings (Dokumenten)
str_list = ["Ich liebe NLP. Text und Sprache ist super. :-)",
"NLP ist doof",
"Machine Learning ist das Beste. 1000 mal besser als.."]


# =============================================================================
# Großbuchstaben in Kleinbuchstaben umwandeln
# =============================================================================
# Einfache Transformationen mit einem String
"HAllo".lower() # Hier wird die Methode str.lower verwendet

# Als sog list comprehension (kurzschreibweise für eine Schleife) 
# für alle Dokumente
[X.lower() for X in str_list]
   
# =============================================================================
#  Entferne sogenannte stopwords
# =============================================================================
mystopwords = stopwords.words("german")

# Gebe p wieder für p im Dokument, wenn es nicht in meinen Stopwords ist
# Output ist eine Liste
# list_x = [p for p in str_list[0].split()] # nur zum Verständnis

list_x = [p for p in str_list[0].split() if p not in mystopwords]

# Schreibe es wieder in einen String
" ".join(list_x)

# Schreibe eine funktion die stopwords aus einem String entfernt
def stop_func(frase):
    list_x = [p for p in frase.split() if p not in mystopwords]
    return " ".join(list_x)  

# Für einen string
stop_func(str_list[2])

# Als list comprehension
[stop_func(X) for X in str_list]

# =============================================================================
#  Stemming
# =============================================================================

# Instanz des Stemmers erstellen
stemmer=SnowballStemmer("german")

# Funktion zum stemming
def stem_func(frase):
    return " ".join([stemmer.stem(p) for p in frase.split()])       

# Für einen string
stem_func(str_list[2])

# Als list comprehension
[stem_func(X) for X in str_list]


# =============================================================================
# Entferne/Ersetze eine einfache Zeichenfolge
# =============================================================================

# Einfache Transformationen mit Text
"Hallo Welt :-)".replace(":-)", # ersetze das...
                         "-") # ... durch das

# Als list comprehension
[X.replace(":-)", "-") for X in str_list]


# =============================================================================
# Entferne Satzeichen, usw.
# =============================================================================

# In string puctuation befinden sich "alle möglichen" Sonderzeichen
string.punctuation

# Verwende eine Übersezungstabelle
remove_punc = str.maketrans("", # Übersetzungsinput ist gleich
                            "", # ... Übersetzungsoutput
                            string.punctuation)  # all das wird entfernt

# Führe Übersetzung durch
str_list[0].translate(remove_punc) 

# Als list comprehension
[t.translate(remove_punc) for t in str_list]

# =============================================================================
# Entferne Ziffern 0-9
# =============================================================================

# Übersetzungstabelle
remove_digits = str.maketrans("", # Übersetzungsinput
                              "", # Übersetzungsoutput
                              string.digits # all das wird entfernt
                              ) 

# Führe Übersetzung durch
str_list[2].translate(remove_digits) 

# Als list comprehension
[t.translate(remove_digits) for t in str_list]

# =============================================================================
# Mögliche Aufgaben:
# 1. Erstellen Sie selbst eine Liste von Strings.
# 2. Wenden Sie wahlweise einige Vorverarbeitungsschritte an.
# 3. Kombinieren Sie die Schritte zu einer ersten "Pipeline", so dass einige
#     Schritte hintereinander ausgeführt werden.
# =============================================================================

