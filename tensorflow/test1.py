import tensorflow as tf 

# matrix1 = tf.constant([[4,3]])
# matrix2 = tf.constant([[2],[1]])

# product = tf.matmul(matrix1,matrix2)

# state = tf.Variable(0,name='counter')
# # print(state.name)
# one = tf.constant(1)

# new_val = tf.add(state, one)
# update = tf.assign(state, new_val)

# #if inital variable in tensorflow, need to initialize
# init = tf.global_variables_initializer()

# # sess = tf.Session()
# # result = sess.run(product)

# # print(result)
# # sess.close()

# with tf.Session() as sess:
# 	sess.run(init)
# 	for _ in range(3):
# 		sess.run(update)
# 		print(sess.run(state))

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1,input2)

with tf.Session() as sess:
	print(sess.run(output,feed_dict={input1:[7.],input2:[4.]}))