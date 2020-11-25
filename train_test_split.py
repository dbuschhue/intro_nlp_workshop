#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:46:39 2020

@author: David
"""

# train test split 
import pandas as pd
from sklearn.model_selection import train_test_split

# Dataframe
df = pd.read_csv("data_task2_complete.csv")

# Motive Überblick
my_tab = pd.crosstab(index=df["motive"],  # Make a crosstable
                              columns="count") # Name the count column

# Entferne die paar Zeilen mit fehlenden Werten "\\\\N" 
id_x = df[df["motive"] == "\\\\N"].index
df.drop(id_x , inplace = True)

# Split (kleiner Trick: Im Dataset X_train, und X_test sind auch nochmals die
# y-Werte enthalten)
X_train, X_test, y_train, y_test = train_test_split(df,df["motive"], test_size=0.33, 
                                                    random_state=42)
# Speichern
X_train.to_csv("df_train.csv", index = False)
X_test.to_csv("df_test.csv", index = False)