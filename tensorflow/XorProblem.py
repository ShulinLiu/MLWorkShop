# Mar 2nd, 2018
# Neural Networks: tensorflow eamples
# Xor 2 x 3 x 1 layer
import matplotlib as mpl
mpl.use('TkAgg')

import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np 
 
# Dataset definition
X = [[0,0],[0,1],[1,0],[1,1]]
Y = [[0],[1],[1],[0]]

# placeholder
x_ = tf.placeholder(tf.float32,shape = [4,2])
y_ = tf.placeholder(tf.float32,shape = [4,1])

# Model definition
# Hidden units
HU = 3
# 1st layer
W1 = tf.Variable(tf.random_uniform([2,HU],-1.0,1.0))
b1 = tf.Variable(tf.zeros([HU]))
O = tf.nn.sigmoid(tf.matmul(x_,W1) + b1)#non-linear activation output

# 2nd layer
W2 = tf.Variable(tf.random_uniform([HU,1],-1.0,1.0))
b2 = tf.Variable(tf.zeros([1]))
y = tf.nn.sigmoid(tf.matmul(O,W2) + b2)

# quadratic loss function
cost = tf.reduce_sum(tf.square(y_ - y),reduction_indices=[0])
# optimazing the function cost by gradient descent with learning step 0.1
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cost)

#Create seesion
sess = tf.Session()
# initialize variables
sess.run(tf.initialize_all_variables())

# Training
Epochs = 5000

for i in range(Epochs):
	sess.run(train_step,feed_dict={x_:X,y_:Y})
	if i%100 == 0:
		print('Epochs ',i)
		print('cost ',sess.run(cost,feed_dict = {x_:X,y_:Y}))

correct_prediction = abs(y_ - y) < 0.5
cast = tf.cast(correct_prediction,"float")
accuracy = tf.reduce_mean(cast)

yy,aa = sess.run([y,accuracy],feed_dict = {x_:X,y_:Y})

print("Output: ",yy)
print("Accuracy: ",aa)

# draw separation surfaces
plt.figure()
# Platting database
c1 = plt.scatter([1,0],[0,1],marker='s',color='gray',s=100)
c0 = plt.scatter([1,0],[1,0],marker='^',color='gray',s=100)
# Generationg point in [-1,2]x[-1,2]
DATA_x = (np.random.rand(10**6,2)*3) - 1
DATA_y = (sess.run(y,feed_dict={x_:DATA_x}))
# Selecting borderline predictions
ind = np.where(np.logical_and(0.49<DATA_y,DATA_y<0.51))[0]
DATA_ind = DATA_x[ind]
# Plottiong separation surfaces
ss = plt.scatter(DATA_ind[:,0],DATA_ind[:,1],marker='_',color='black',s=5)
plt.legend((c1,c0,ss),('Class 1','Class 0','Separation surfaces'),scatterpoints=1)
plt.xlabel('Input x1')
plt.ylabel('Input x2')
plt.axis([-1,2,-1,2])
plt.show()