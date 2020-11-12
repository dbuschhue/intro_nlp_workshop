# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 10:14:39 2020

@author: Workshopteam NLP in Bildungsforschung
"""

import os
import re
import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sklearn
import umap
import hdbscan
from sentence_transformers import SentenceTransformer, models

import pyLDAvis
from sklearn.decomposition import LatentDirichletAllocation as LDA
from pyLDAvis import sklearn as sklearn_lda

# Der folgende Befehl lädt das vortrainierte Sprachmodell
# Das Sprachmodell wird dann lokal auf Ihrer Festplatte gespeichert, sodass Sie es zum Workshop schnell laden können
word_embedding_model = models.Transformer('bert-base-german-cased', max_seq_length=256) 

# data = pd.read_csv('...')

print( 'Everything worked! - You are ready to go.' )
