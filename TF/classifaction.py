import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score,precision_score,confusion_matrix,f1_score,recall_score
from sklearn.metrics import mean_squared_error,r2_score

df=pd.read_csv('name_file ',sep=',',header=0)

def norm(x):
    return(x-np.min(x))/(np.max(x)-np.min(x))

timesteps = 14

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
Y000=np.array(df.iloc[:,30]).astype(np.float32)
Y0=np.array(pd.get_dummies(Y000))[14:98]

X0=np.array(df.iloc[:,range(12,29)]).astype(np.float32)
vars_num=4
X0=SelectKBest(chi2, k=vars_num).fit_transform(X0, Y000)


X0=norm(X0)[14:98]



import tensorflow as tf
tf.reset_default_graph()


import tensorflow as tf

tf.reset_default_graph()

lr = 0.00001
training_epochs = 20000
batch_size = 84
display_step = 10

n_hidden_1 = 50
n_hidden_2 = 50
n_input = 4 
n_classes = 3 


X = tf.placeholder("float", [None, n_input])
Y = tf.placeholder("float", [None, n_classes])

weights = {
    'h1': tf.Variable(tf.random_uniform([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_uniform([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_uniform([n_hidden_2, n_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_uniform([n_hidden_1])),
    'b2': tf.Variable(tf.random_uniform([n_hidden_2])),
    'out': tf.Variable(tf.random_uniform([n_classes]))
}


def multilayer_perceptron(x):
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer

def next_batch(num, data, labels):
    idx = np.arange(0 , len(data))
    np.random.shuffle(idx)
    idx = idx[:num]
    data_shuffle = [data[ i] for i in idx]
    labels_shuffle = [labels[ i] for i in idx]
    return np.asarray(data_shuffle), np.asarray(labels_shuffle)

logits = multilayer_perceptron(X)

loss1 = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=logits, labels=Y))
global_step = tf.Variable(0, trainable=False)

optimizer = tf.train.AdamOptimizer(learning_rate=lr)
train1 = optimizer.minimize(loss1)

prediction = tf.nn.softmax(logits)  
init = tf.global_variables_initializer()


with tf.Session() as sess:
    sess.run(init)
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(len(Y0)/batch_size)
        Xt, Yt = next_batch(batch_size, X0, Y0)
        for i in range(total_batch):
            batch_x, batch_y = Xt,Yt
            _, c = sess.run([train1, loss1], feed_dict={X: batch_x,Y:batch_y})
            avg_cost += c / total_batch
        if epoch % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost={:.9f}".format(avg_cost))
    print("Optimization Finished!")
    output = sess.run([prediction],feed_dict={X: X0})

pred0=np.argmax(output,axis=2)[0]


print('Accuracy:',accuracy_score(np.array(Y000[14:98]),pred0))
print('Precision (FP):',precision_score(np.array(Y000[14:98]),pred0,average='macro'))
print('Recall (FN):',recall_score(np.array(Y000[14:98]),pred0,average='macro'))
print('f1:',f1_score(np.array(Y000[14:98]),pred0,average='macro'))
print(confusion_matrix(np.array(Y000[14:98]),pred0),'\n')