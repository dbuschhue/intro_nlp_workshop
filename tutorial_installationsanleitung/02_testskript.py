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

word_embedding_model = models.Transformer('bert-base-german-cased', max_seq_length=256) # dieser Befehl lädt das vortrainierte Sprachmodell

# data = pd.read_csv('...')

print( 'Everything worked! - You are ready to go.' )
