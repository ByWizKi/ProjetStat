#coding:utf-8

#Import
import numpy as np
import matplotlib.pyplot as plt
import pandas as pan
import scipy.stats as st
import statsmodels.api as sm
from math import sqrt



# Exo : 1

#Chargement des donnees
Air = pan.read_csv("http://tinyurl.com/y39an7ef/Data89965.csv", sep='\t', na_values='-')

#Affichage de l'entetes
# Air.info()

#Affichage de max date et min date
minDate = Air.iloc[0][0]
maxDate = Air.iloc[730][0]

#Calcule le nombre de jour ou toutes les stations on mesure leur PM10
nbGrenoblePM10 = Air['Date'].count() - Air['Grenoble Rocade Sud Particules PM10'].count() -1
nbClermontPM10 = Air['Date'].count() - Air['Clermont-Fd A71 Particules PM10'].count() -1
nbLyonPM10 = Air['Date'].count() - Air['A7 Sud lyonnais Particules PM10'].count() -1
nbIserePm10 = Air['Date'].count() - Air['A7 Nord-Isere Particules PM10'].count() -1
nbPM10 = Air['Date'].count() - (nbClermontPM10+nbGrenoblePM10+nbLyonPM10+nbIserePm10) -1

#
TC= Air.isna().value_counts() 
print(TC)