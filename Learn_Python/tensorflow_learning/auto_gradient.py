import tensorflow as tf


def test_gradient_tape():
    w = tf.Variable(tf.random.normal((3, 2)), dtype=tf.float32, name='w')
    b = tf.Variable(tf.zeros(2, dtype=tf.float32), name='b')
    x = tf.constant([[1., 2., 3.]], dtype=tf.float32)

    with tf.GradientTape(persistent=True) as tape:
        y = x @ w + b
        loss = tf.reduce_mean(y**2)

    [dl_dw, dl_db] = tape.gradient(loss, [w, b])
    print(type(tape.gradient(loss, [w, b])[0]))
    print(dl_dw)
    print(dl_db)
    print(tape.watched_variables()[0])
    print(type(tape.watched_variables()))


def test_trainable():
    # A trainable variable
    x0 = tf.Variable(3.0, name='x0')
    # Not trainable
    x1 = tf.Variable(3.0, name='x1', trainable=False)
    # Not a Variable: A variable + tensor returns a tensor.
    x2 = tf.Variable(2.0, name='x2') + 1.0
    # Not a variable
    x3 = tf.constant(3.0, name='x3')

    with tf.GradientTape() as tape:
        y = (x0**2) + (x1**2) + (x2**2)

    grad = tape.gradient(y, [x0, x1, x2, x3])

    for g in grad:
        print(g)


if __name__ == '__main__':
    print("tensorflow version is", tf.__version__)

    test_gradient_tape()
    test_trainable()
