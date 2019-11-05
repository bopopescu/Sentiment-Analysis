import gensim.models.keyedvectors as word2vec
import numpy as np
model_embedding = word2vec.KeyedVectors.load('./word.model')

word_labels = []
max_seq = 200
embedding_size = 128

for word in model_embedding.vocab.keys():
    word_labels.append(word)


def comment_embedding(comment):
    matrix = np.zeros((max_seq, embedding_size))
    words = comment.split()
    lencmt = len(words)

    for i in range(max_seq):
        if lencmt == 0:
            continue
        indexword = i % lencmt
        if (max_seq - i < lencmt):
            break
        if (words[indexword] in word_labels):
            matrix[i] = model_embedding[words[indexword]]
    matrix = np.array(matrix)
    return matrix