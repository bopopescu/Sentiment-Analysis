from tensorflow import keras
import converToMatrix as ctm
import numpy as np
import os
import Process as pr


model_sentiment = keras.models.load_model('./models.h5')

text = "....têt"
text = pr.pre_process(text)
print(text)

maxtrix_embedding = np.expand_dims(ctm.comment_embedding(text), axis=0)
maxtrix_embedding = np.expand_dims(maxtrix_embedding, axis=3)

result = model_sentiment.predict(maxtrix_embedding)
result = np.argmax(result)
print("Label predict: ", result)
