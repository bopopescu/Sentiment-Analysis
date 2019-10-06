from tensorflow import keras
import converToMatrix as ctm
import numpy as np
model_sentiment = keras.models.load_model('./models.h5')

def pre_process(text):
# các bạn tự thêm các tiền xử lý của mình vào đây nhá
    return text

text = "đồ ăn ở đây vừa nhiều vừa ngon"
#text = pre_process(text)

maxtrix_embedding = np.expand_dims(ctm.comment_embedding(text), axis=0)
maxtrix_embedding = np.expand_dims(maxtrix_embedding, axis=3)

result = model_sentiment.predict(maxtrix_embedding)
result = np.argmax(result)
print("Label predict: ", result)
