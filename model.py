from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
import operator
import functools
from ntpath import join
import pandas as pd
import joblib
import numpy as np
import mysql.connector
from pathlib import Path
import os
from os import popen
import sys

dbase = mysql.connector.connect(
    host='localhost',
    database='tb_berkas',
    user='root',
    password=''
)

mycursor = dbase.cursor()

umur = dbase.cursor()
umur.execute(
    "SELECT nama from tb_berkas ORDER BY id desc limit 1")
hasil = umur.fetchone()
# print(hasil)


def convertTuple(tup):
    str = functools.reduce(operator.add, (tup))
    return str


file = (hasil)
str = convertTuple(file)
direktori = ('berkas/', str)
dataset = convertTuple(direktori)
print(dataset)

# if str == csv:
# data = pd.read_csv(dataset)
# else:
# data = pd.read_excel(dataset)
data = pd.read_csv(dataset)

# print(data)
model_file = 'model/classification_model.sav'
loaded_model = joblib.load(model_file)

features = data.loc[:, 'MD':'P3_(SKOR JANG)'].values

# scaler = preprocessing.MinMaxScaler(feature_range=(0, 10)).fit(features)
# scaled_feature = scaler.transform(features)

result = loaded_model.predict(features)

hasil = pd.DataFrame(result)
nip = data['NIP']
name = data['NAME']
df = pd.concat([nip, name, hasil], axis=1)

dada = pd.DataFrame(df)
print(dada)
