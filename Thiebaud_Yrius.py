# # coding:utf-8

# Import
import numpy as np
import matplotlib.pyplot as plt
import pandas as pan
import dataframe_image as dfi
import scipy.stats as st
import statsmodels.api as sm
import scipy.stats.mstats as ms


# Exo : 1

# Chargement des donnees

Air = pan.read_csv("http://tinyurl.com/y39an7ef/Data89965.csv", sep='\t', na_values='-')


### Question 1 ###

typeAir = Air.dtypes

### Question 2 ###


# Fonction qui calcule le nombre de jour ou les PM10 ont ete messure a toutes les stations

def sumDayPM10():
    nbDay = 0
    for i in range(0, 731):
        if (Air.isna()).iloc[i, 3] != True and (Air.isna()).iloc[i, 7] != True and (Air.isna()).iloc[i, 11] != True and (Air.isna()).iloc[i, 15] != True:
            nbDay += 1
    return nbDay

### Question 3 ###

def checkPM():
    result = []
    for i in range(0, 731):
        if (Air.isna()).iloc[i, 3] != True and (Air.isna()).iloc[i, 4] != True and (Air.isna()).iloc[i, 7] != True and (Air.isna()).iloc[i, 8] != True and (Air.isna()).iloc[i, 11] != True and (Air.isna()).iloc[i, 12] != True and (Air.isna()).iloc[i, 15] != True:
            result.append(True)
        else:
            result.append(False)
    return result

def checkAzote():
    result = []
    for i in range(0, 731):
        if (Air.isna()).iloc[i, 1] != True and (Air.isna()).iloc[i, 2] != True and (Air.isna()).iloc[i, 5] != True and (Air.isna()).iloc[i, 6] != True and (Air.isna()).iloc[i, 9] != True and (Air.isna()).iloc[i, 10] != True and (Air.isna()).iloc[i, 13] != True and (Air.isna()).iloc[i, 14] != True:
            result.append(True)
        else:
            result.append(False)
    return result

# les valeurs seront automatiquemt de type bool pas besoin de convertion

Air = Air.assign(PMObs=checkPM())
Air = Air.assign(AzoteObs=checkAzote())

# Affiche la table de contingence de PMObs et AzoteObs

table = pan.crosstab(Air['PMObs'], Air['AzoteObs'])

### Question 4 ###

colPM10 = Air['A7 Sud lyonnais Particules PM10'].dropna()

# fonction qui renvoie un tuples avec la moyenne les variances et le quartiles 25%

def infoData(data):
    moyData = np.mean(data)
    vData = np.var(data, ddof=0)
    varData = np.var(data, ddof=1)
    quarData = np.quantile(data, [0.25])
    return moyData, vData, varData, quarData[0]


infoPM10 = infoData(colPM10)

### Question 5 ###

def checkPM10(val):
    result = []
    for i in range(0, 731):
        if Air['A7 Sud lyonnais Particules PM10'][i] > val:
            result.append(1)
        else:
            result.append(0)
    return result


Air = Air.assign(seuilInfo=checkPM10(50.0))
Air = Air.assign(seuilAlerte=checkPM10(80.0))

### Question 6 ###

def interConf(data):
    inter = st.binomtest(k=np.sum(data), n=len(data)).proportion_ci(confidence_level=0.95, method='exact')
    return inter


PseuilInfo = interConf(Air['seuilInfo']) #intervalle de confiance exact a 0.95 pour seuilInfo

seuilAlert = interConf(Air['seuilAlerte']) #intervalle de confiance exact a 0.95 pour seuilAlerte

### Question 7 ###

testAlternative = st.ttest_1samp(Air['seuilInfo'], popmean=35/365, alternative='two-sided')


### Question 8 ###

testSignificative = st.ttest_1samp(Air['seuilInfo'], popmean=35/365, alternative='greater')


### Question 9 ###

def ajoutAzotePM(indiceCol1, indiceCol2):
    result = []
    for i in range(0, 731):
        
        if (Air.isna()).iloc[i, indiceCol1] != True or (Air.isna().iloc[i, indiceCol2]) != True:
            result.append(Air.iloc[i, indiceCol1]+Air.iloc[i, indiceCol2])
        else:
            result.append(np.nan)
    return result

grenobleAzote = ajoutAzotePM(1, 2)
grenoblePM = ajoutAzotePM(3, 4)

a7NordAzote = ajoutAzotePM(5, 6) 
a7NordPM = ajoutAzotePM(7, 8)

a7SudAzote = ajoutAzotePM(9, 10)
a7SudPM = ajoutAzotePM(11, 12)

clermontAzote = ajoutAzotePM(13, 14)

dfs = pan.DataFrame({'Date':Air['Date'],
                       'Grenoble Rocade Sud Oxyde d\'azote':grenobleAzote,
                       'Grenoble Rocade Sud PM':grenoblePM,
                       'A7 Nord-Isere Oxyde d\'azote': a7NordAzote,
                       'A7 Nord-Isere PM': a7NordPM,
                       'A7 Sud lyonnais Oxyde d\'azote':a7SudAzote,
                       'A7 Sud lyonnais PM':a7SudPM,
                       'Clermont-Fd A71 Oxyde d\'azote': clermontAzote}).dropna()
#saveCovariance = dfi.export(dfs.cov(), 'covarianceMatrix.png')

### Question 10 ###
def convertData(indiceCol):
    result = []
    for i in range(0, len(dfs)):
        result.append(np.log(float(dfs.iloc[i, indiceCol]))) 
    return result

x = convertData(2)
y = convertData(6)

cor = st.pearsonr(x, y)


# Exo : 2

### Question 1 ###

U = st.uniform.rvs(0, 1, size=10000)
S = (-np.log(U)*10)
R = np.ceil(S)
V=S[S>0]
# plt.hist(V, density=True, color='red')
# plt.xlabel("S positif")
# plt.ylabel("Densite")
# plt.show()

### Question 2 ###



### Question 3 ###

def Q3():
    plt.plot(R)
    plt.show()
Q3()

### Question 4 ###

### Question 5 ###

### Question 6 ###