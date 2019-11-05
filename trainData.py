import numpy as np
from tensorflow.python.keras import layers
from tensorflow import keras
import tensorflow as tf
import converToMatrix as ctm
from tqdm import tqdm
import word2vec as wc

sequence_length = 200
embedding_size = 128
num_classes = 3
filter_sizes = 3
num_filters = 150
epochs = 50
batch_size = 30
learning_rate = 0.01
dropout_rate = 0.5
path = './data/'

train_data = []
label_data = []

pre_reviews, labels = wc.readdata(path)

for x in tqdm(pre_reviews):
    train_data.append(ctm.comment_embedding(x))
train_data = np.array(train_data)

for y in tqdm(labels):
    label_ = np.zeros(3)
    try:
        label_[int(y)] = 1
    except:
        label_[0] = 1
    label_data.append(label_)


x_train = train_data.reshape(train_data.shape[0], sequence_length, embedding_size, 1).astype('float32')
y_train = np.array(label_data)

# Define model
model = keras.Sequential()
#model = keras.optimizers.Adam(lr=0.001)
model.add(layers.Convolution2D(num_filters, (filter_sizes, embedding_size),
                        padding='valid',
                        input_shape=(sequence_length, embedding_size, 1), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(198, 1)))
model.add(layers.Dropout(dropout_rate))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(3, activation='softmax'))
# Train model
#adam = tf.train.AdamOptimizer()
adam = tf.keras.optimizers.Adam(lr=0.001)
model.compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=['accuracy'])
print(model.summary())
#9725 label => train 70%, validation 30%
model.fit(x = x_train[:7000], y = y_train[:7000], batch_size = batch_size, verbose=1, epochs=epochs, validation_data=(x_train[:2725], y_train[:2725]))

model.save('models.h5')
