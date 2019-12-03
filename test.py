from tensorflow import keras
import converToMatrix as ctm
import numpy as np
import os
import Process as pr
import tensorflow as tf


# model_sentiment = keras.models.load_model('./models.h5')
model_sentiment = tf.keras.models.load_model('./models.h5', compile=False)

# Show the model architecture
model_sentiment.summary()

text = "quán này ngày_càng ngon"
text = pr.pre_process(text)
print(text)
#
maxtrix_embedding = np.expand_dims(ctm.comment_embedding(text), axis=0)
maxtrix_embedding = np.expand_dims(maxtrix_embedding, axis=3)
#
result = model_sentiment.predict(maxtrix_embedding)
print(result)
result = np.argmax(result)
print("Label predict: ", result)



