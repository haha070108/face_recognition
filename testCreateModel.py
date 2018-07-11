from tensorflow.python.platform import gfile
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
num =tf.Variable(1,name="count")
new_value=tf.add(num,10)
op = tf.assign(num,new_value)

session =tf.Session()
session.run(tf.global_variables_initializer())
print(session.run(num))
for i in range(5):
    session.run(op)
    print(session.run(num))

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
new_value = tf.multiply(input1, input2)
print(type(new_value))
result =session.run(new_value,feed_dict={input1:25,input2:2})
print(result)
session.close()
