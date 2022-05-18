import numpy as np
import tensorflow as tf


class DCN(object):
    def __init__(self, vec_dim=None, field_lens=None, cross_layer_num=None, dnn_layers=None, lr=None,
                 dropout_rate=None):
        self.vec_dim = vec_dim
        self.field_lens = field_lens
        self.field_num = len(field_lens)
        self.feat_num = np.sum(field_lens)
        self.cross_layer_num = cross_layer_num
        self.dnn_layers = dnn_layers
        self.lr = lr
        self.dropout_rate = dropout_rate
        self.index = tf.Tensor(tf.int32, shape=[None, self.field_num], name='feat_index')  # (batch, F)
        self.x = tf.Tensor(tf.float32, shape=[None, self.field_num], name='feat_value')  # (batch, F)
        self.y = tf.Tensor(tf.float32, shape=[None], name='input_y')
        self.is_train = tf.Tensor(tf.bool)
        self.y_hat = tf.nn.sigmoid(self.y_logits)
        self.pred_label = tf.cast(self.y_hat > 0.5, tf.int32)
        self.loss = -tf.reduce_mean(self.y * tf.log(self.y_hat + 1e-8) + (1 - self.y) * tf.log(1 - self.y_hat + 1e-8))
        self.train_op = tf.train.AdamOptimizer(self.lr).minimize(self.loss)
        with tf.variable_scope('emb_part'):
            embed_matrix = tf.get_variable(name='second_ord_v', shape=[self.feat_num, self.vec_dim], dtype=tf.float32)
            embed_v = tf.nn.embedding_lookup(embed_matrix, self.index)  # (batch, F, K)
            embed_x = tf.multiply(tf.expand_dims(self.x, axis=2), embed_v)  # (batch, F, K)
            embed_x = tf.layers.dropout(embed_x, rate=self.dropout_rate, training=self.is_train)  # (batch, F, K)
            node_num = self.field_num * self.vec_dim
            embed_x = tf.reshape(embed_x, shape=(-1, node_num))  # (batch, node_num)

        with tf.variable_scope('cross_part'):
            cross_vec = embed_x
            for i in range(self.cross_layer_num):
                cross_vec = self.cross_layer(embed_x, cross_vec, 'cross_layer_%d' % i)  # (batch, node_num)

        with tf.variable_scope('dnn_part'):
            dnn = embed_x
            in_num = node_num
            for i in range(len(self.dnn_layers)):
                out_num = self.dnn_layers[i]
                w = tf.get_variable(name='w_%d' % i, shape=[in_num, out_num], dtype=tf.float32)
                b = tf.get_variable(name='b_%d' % i, shape=[out_num], dtype=tf.float32)
                dnn = tf.matmul(dnn, w) + b
                dnn = tf.layers.dropout(tf.nn.relu(dnn), rate=self.dropout_rate, training=self.is_train)
                in_num = out_num

        with tf.variable_scope('output_part'):
            in_num += node_num
            output = tf.concat([cross_vec, dnn], axis=1)
            proj_w = tf.get_variable(name='proj_w', shape=[in_num, 1], dtype=tf.float32)
            self.y_logits = tf.matmul(output, proj_w)

    def cross_layer(self, x0, xl, name):
        with tf.variable_scope(name):
            node_num = self.field_num * self.vec_dim
            w = tf.get_variable(name='w', shape=[node_num], dtype=tf.float32)
            b = tf.get_variable(name='b', shape=[node_num], dtype=tf.float32)
            xl_w = tf.tensordot(xl, w, axes=[1, 0])  # (batch, )
            x0_xl_w = tf.multiply(x0, tf.expand_dims(xl_w, -1))  # (batch, node_num)
            x = tf.add(x0_xl_w, b)  # (batch, node_num)
            x = x + xl  # (batch, node_num)
        return x
