# -*- coding: utf-8 -*-
# Read list comment file
from gensim.models import Word2Vec
import os
import pandas as pd

path = './data/'


def readdata(path):
    list_file = os.listdir(path)
    data = pd.DataFrame()
    for filename in list_file:
        data = pd.concat([data, pd.read_csv(os.path.join(path, filename), sep=',')])
    return data.Review, data.Label


reviews, label = readdata(path)
input_gensim = []
for review in reviews:
    print(review)
    input_gensim.append(review.split())

model = Word2Vec(input_gensim, size=128, window=5, min_count=0, workers=4, sg=1)
model.wv.save("word.model")
print("OKE")