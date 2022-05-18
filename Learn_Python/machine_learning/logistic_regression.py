import numpy as np


class LogisticRegression():
    def __init__(self, num_feature: int, learning_rate: float) -> None:
        '''
        Constructor
        Parameters:
          num_features is the number of features.
          learning_rate is the learning rate.
        Return:
          there is no return value.
        '''
        self.num_feature = num_feature
        self.w = np.random.randn(num_feature + 1)
        self.learning_rate = learning_rate

    def artificial_feature(self, x: np.ndarray) -> np.ndarray:
        '''
        add one artificial features to the data input
        Parameters:
          x is the data input. x is one dimensional or two dimensional numpy array.
        Return:
          updated data input with the last column of x being 1s.
        '''
        if len(x.shape) == 1:  # if x is one dimensional, convert it to be two dimensional
            x = x.reshape((1, -1))
        # write your code below #

        last_column = np.array([1] * len(x))
        X = np.column_stack((x, last_column))

        # write yoru codel
        return X

    def sigmoid(self, x: np.ndarray) -> np.ndarray:
        '''
        Compute sigmoid activation function value by f(x*w)
        Parameters:
          x is data input with artificial features. x is a two dimensional numpy array.
        Return:
          one dimensional numpy array
        '''
        # write your code below #
        # first compute inner product between x and self.w
        # sencond, compute logistic function value of x*self.w

        w_x = np.matmul(x, self.w)

        beta = np.max(w_x)
        prob = np.exp(w_x - beta) / (np.exp(-beta) + np.exp(w_x - beta))

        if np.all(w_x) >= 0:
            prob = 1 / (1 + np.exp(-w_x))
        else:
            prob = np.exp(w_x) / (np.exp(w_x) + 1)

        # write your code above #
        return prob

    def predict(self, X: np.ndarray) -> np.ndarray:
        '''
        Predict label probability for the input X
        Parameters:
          X is the data input. X is one dimensional or two dimensional numpy array.
        Return: 
          predicted label probability, which is a one dimensional numpy array.
        '''
        X = self.artificial_feature(X)
        # write your code below #

        prob = self.sigmoid(X)

        # write your code above #
        return prob

    def loss(self, y: np.ndarray, prob: np.ndarray) -> float:
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

        eposilon = pow(10, -5)
        prob[np.where(prob < eposilon)] = eposilon
        prob[np.where(prob > 1 - eposilon)] = 1 - eposilon

        loss_value = -sum(y * np.log(prob) + (1 - y) * np.log(1 - prob))

        # write your code above #
        return loss_value

    def gradient(self, trainX: np.ndarray, trainY: np.ndarray) -> np.ndarray:
        '''
        Compute gradient of logistic regression.
        Parameters:
          trainX is the training data input. trainX is a two dimensional numpy array.
          trainY is the training data label. trainY is a one dimensional numpy array.
        Return:
          a one dimensional numpy array representing the gradient
        '''
        x = self.artificial_feature(trainX)
        # write your code below #

        prob = self.predict(trainX)
        g = np.sum(np.matmul(-trainY + prob, x), axis=0)

        # write your code above #
        return g

    def update_weight(self, dLdw: np.ndarray) -> None:
        '''
        Update parameters of logistic regression using the given gradient.
        Parameters:
          dLdw is a one dimensional gradient.
        Return:
          there is no return value
        '''
        self.w += -self.learning_rate*dLdw
        return

    def one_epoch(self, X: np.ndarray,  Y: np.ndarray, batch_size: int, train: bool = True) -> tuple:
        '''
        One epoch of either training or testing procedure.
        Parameters:
          X is the data input. X is a two dimensional numpy array.
          Y is the data label. Y is a one dimensional numpy array.
          batch_size is the number of samples in each batch.
          train is a boolean value indicating training or testing procedure.
        Returns:
          loss_value is the average loss function value.
          acc is the prediction accuracy.        
        '''
        num_sample = X.shape[0]  # number of samples
        num_correct = 0        # number of corrected predicted samples
        num_batch = int(num_sample/batch_size)+1  # number of batch
        # index for each batch
        batch_index = list(gen_batches(num_sample, num_batch))
        loss_value = 0  # loss function value
        for i, index in enumerate(batch_index):  # the ith batch
            x, y = X[index, :], Y[index]  # get a batch of samples
            if train:
                dLdw = self.gradient(x, y)  # compute gradient
                self.update_weight(dLdw)   # update parameters of the model
            prob = self.predict(x)        # predict the label probability
            # loss function value for ith batch
            loss_value += self.loss(y, prob)*x.shape[0]
            num_correct += self.accuracy(y, prob)*x.shape[0]
        loss_value = loss_value/num_sample  # average loss
        acc = num_correct/num_sample       # accuracy
        return loss_value, acc

    def accuracy(self, y: np.ndarray, prob: np.ndarray) -> float:
        '''
        compute accuracy
        Parameters:
          y is the true label. y is a one dimensional array.
          prob is the predicted label probability. prob is a one dimensional array.
        Return:
          acc is the accuracy value
        '''
        # write your code below #

        prob[np.where(prob <= 0.5)] = 0
        prob[np.where(prob >= 0.5)] = 1

        acc = sum(y == prob) / len(y)

        # write your code above #
        return acc
