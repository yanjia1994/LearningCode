import tensorflow as tf


class DCN3:
    def __init__(self, cross_layer_num=None, dense_layer_count=None):
        self.cross_layer_num = cross_layer_num
        self.dense_layer_count = dense_layer_count

    @staticmethod
    def cross_layer(x0, xl):
        """
        实现一层cross layer
        @param x0: 特征embeddings
        @param xl: 前一层的输出结果
        """

        # 1.获取xl层的embedding size,用于生成初始化的参数w,b的shape
        embed_dim = xl.shape[-1]

        # 2.初始化当前层的W和b
        w = tf.Variable(tf.random.truncated_normal(shape=(embed_dim,), stddev=0.01))
        b = tf.Variable(tf.zeros(shape=(embed_dim,)))

        # 3.计算feature crossing
        xl_t = tf.reshape(xl, [-1, 1, embed_dim])  # reshape操作相当于将列向量转换为行向量
        xl_w = tf.tensordot(xl_t, w, axes=1)  # 行向量与列向量的乘积结果是一个标量, (None,1)
        cross = x0 * xl_w + b + xl

        return cross

    def cross_network(self, x0):
        """
        构建多层 cross network
        param x0: 所有特征的embeddings
        """

        cross_network_output = x0
        for _ in range(self.cross_layer_num):
            cross_network_output = self.cross_layer(x0, cross_network_output)

        return cross_network_output

    def dense_network(self, x0):
        """
        构建多层 dense network
        @param x0: 所有特征的embeddings
        @return: 
        """

        fc_layer_output = x0
        for dense_layer_num in range(self.dense_layer_count):
            fc_layer_output = tf.keras.Dropout(0.5)(tf.keras.Dense(dense_layer_num, activation='relu')(fc_layer_output))

        return fc_layer_output

    def combination_layer(self, x0):
        cross_network_output = self.cross_network(x0)
        fc_layer_output = self.dense_network(x0)
        stack_layer = tf.concat([cross_network_output, fc_layer_output], axis=1)
        combination_layer_input_dim = stack_layer.shape[-1]

        w = tf.Variable(tf.random.truncated_normal(shape=(combination_layer_input_dim,), stddev=0.01))
        b = tf.Variable(tf.zeros(shape=(combination_layer_input_dim,)))
        output_layer = tf.sigmoid(tf.matmul(stack_layer, w) + b)

        # output_layer = tf.keras.Dense(1, activation='sigmoid', use_bias=True)(stack_layer)

        return output_layer
