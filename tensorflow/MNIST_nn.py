# import
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from sklearn.metrics import confusion_matrix

# load data
from tensorflow.examples.tutorials.mnist import input_data
data = input_data.read_data_sets("data/MNIST/", one_hot=True)

# define two functions
def init_weight(shape):
	return tf.Variable(tf.random_uniform(shape,-0.1,0.1))

def mlp_output(X, W_h, W_o, b_h, b_o):
	a1 = tf.matmul(X, W_h) + b_h
	o1 = tf.nn.relu(a1) #output layer1
	a2 = tf.matmul(o1, W_o) + b_o
	o2 = tf.nn.relu(a2) #output layer1
	 
	return o2

W1 = init_weight([x_dim,h_layer_dim])