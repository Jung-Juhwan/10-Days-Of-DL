import tensorflow as tf

"""
Lab1 basic 
change existing lab1 code to tensorflow version 2
existing code ; node1+node2
"""

#make constant
node1= tf.constant(3)
node2=tf.constant(4)

node3=node1+node2

print(node3)

@tf.function # Use instead of Session()
def add(x,y):
    return x+y

print(add(tf.Variable(3),node2))
