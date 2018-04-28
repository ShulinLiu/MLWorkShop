import tensorflow as tf 

# initialize two constants
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

# multiply
result = tf.multiply(x1,x2)

# print(result)
# Tensor("Mul:0", shape=(4,), dtype=int32)

# ############### model 1 #################
# # initialize the session
# sess = tf.Session()

# # print result
# print(sess.run(result))

# # close the session
# sess.close()
# ##########################################

############### model 2 #################
# initialize the session
with tf.Session() as sess:
	output = sess.run(result)
	print(output)
##########################################

# with tf.Session() as sess:
# 	with tf,device("/gpu:1"):
# 		matrix1 = tf.constant([[3.,3.]])
# 		matrix2 = tf.constant([[2.],[2.]])
# 		product = tf.matmul(matrix1,matrix2)
# 		print(product)