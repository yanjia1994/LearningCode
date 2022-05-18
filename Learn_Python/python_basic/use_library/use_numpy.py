import numpy as np


def artificial_feature(x):
    """
    add one artificial features to the data input
    Parameters:
        x is the data input. x is one dimensional or two dimensional numpy array.
    Return:
        updated data input with the last column of x being 1s.
    """
    if len(x.shape) == 1:
        x = x.reshape((1, -1))

    last_column = np.array([1] * len(x))
    X = np.column_stack((x, last_column))
    return X


def loss(y, prob):
    '''
    Compute cross entropy loss.
    Parameters:
        y is the true label. y is a one dimensional array.
        prob is the predicted label probability. prob is a one dimensional array.
    Return:
        cross entropy loss
    '''
    # write your code below #
    # you must think of how to deal with the case that prob contains 1 or 0 #
    eposilon = pow(10, -10)
    prob[prob < eposilon] = eposilon
    prob[prob > 1 - eposilon] = 1 - eposilon
    print(y * np.log(prob))

    loss_value = -sum(y * np.log(prob) + (1 - y) * np.log(1 - prob))

    # write your code above #
    return loss_value


def accuracy(y, prob):
    '''
    compute accuracy
    Parameters:
        y is the true label. y is a one dimensional array.
        prob is the predicted label probability. prob is a one dimensional array.
    Return:
        acc is the accuracy value
    '''
    # write your code below #
    prob[prob <= 0.5] = 0
    prob[prob >= 0.5] = 1

    acc = sum(y == prob) / len(y)

    # write your code above #
    return acc


if __name__ == '__main__':
    x = np.arange(15).reshape(3, 5)
    w = np.array([2] * len(x[0]))
    w_ = np.array([1, 2, 3, 4, 5])
    eposilon = pow(10, -5)
    xx = np.array([0.0, 1., 2])
    print(eposilon)
    xx[xx < eposilon] = eposilon
    xx[xx > 1 - eposilon] = 1 - eposilon

    y = np.array([0., 0., 0., 0., 1., 0., 0., 1., 1., 0., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1., 1., 1., 1., 0., 1., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 1., 1., 1., 0., 1., 1., 0., 0., 0., 1., 1., 1., 0.,
                  0., 0., 0.])
    prob = np.array([1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 9.9999e-01, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 9.9999e-01, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05,
                     1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 9.9999e-01, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05, 1.0000e-05])

    y = np.array([0., 1.])
    prob = np.array([1.0000e-05, 0.4])

    arr1 = np.array([np.arange(5), np.arange(5)])
    print(arr1)

    print("accuracy = ", accuracy(y, prob))
    print(type(y))
    print(len(prob))
    print(loss(y, prob))
    print(xx)
    print(w * w_)
    print("x = ", x.shape)
    print("w = ", w.shape)

    # numpy ndarray的创建
    # 1. 基于列表或者元组
    arr_list_1 = np.array([0, 1, 2])
    arr_list_2 = np.array([[0, 1], [1, 2]])
    arr_list_2.shape = (1, 4)
    print("arr_list_1 = ", arr_list_1)
    print("arr_list_2 = ", arr_list_2)
    arr = np.arange(6).reshape(2, 3)
    arr_2 = np.arange(3).reshape(3, 1)
    print(arr)
    print(arr_2)
    print(arr @ arr_2)
    print(np.matmul(arr, arr_2))
    print(np.dot(arr, arr_2))