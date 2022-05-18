import numpy as np
import tensorflow as tf

print(tf.__version__)

rank_0_tensor = tf.constant(4)
rank_1_tensor = tf.constant([2.0, 3.0, 4.0])
print(np.array(rank_1_tensor))
print(rank_1_tensor.numpy())

rank_2_tensor = tf.constant([[1, 2],
                             [3, 4],
                             [5, 6]], dtype=tf.float16)
rank_3_tensor = tf.constant([[[0, 1, 2, 3, 4],
                              [5, 6, 7, 8, 9]],
                             [[10, 11, 12, 13, 14],
                              [15, 16, 17, 18, 19]],
                             [[20, 21, 22, 23, 24],
                              [25, 26, 27, 28, 29]]])


print(rank_0_tensor)
print(rank_1_tensor)
print(rank_2_tensor)
print(rank_3_tensor)


print(rank_2_tensor.device)

print(rank_3_tensor.shape)


