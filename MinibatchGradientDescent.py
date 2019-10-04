import numpy as np
import matplotlib.pyplot as plt

# step 1 : create training and testing data and visualize training data.

# creating data
mean = np.array( [5.0, 6.0] )  # mean vector
cov = np.array( [[1.0, 0.95],
                 [0.95, 1.2]] )  # covariance matrix
data = np.random.multivariate_normal( mean, cov, 8000 )  # multivariate normal distribution

# visualising data
plt.scatter( data[:500, 0], data[:500, 1], marker='.' )
plt.show()

# train - test - split
# data.shape # tuple of array dimensions, (8000, 2), data.shape[0] will return first dimension shape, count of rows
# np.ones((10,2),float) #  Return a new array of given shape and type, filled with ones.
#  10 rows, 2 cols, float number
oneColArr = np.ones( (data.shape[0], 1) )
data = np.hstack( (oneColArr, data) )  # add a new column to data to save prediction result

split_factor = 0.90
split = int( split_factor * data.shape[0] )

# first dimension range: 0~ split, second dimension range : stop at last col data[:split, -1]) last col as y,
# its direction is x axis direction, after reshape, it will be y axis direction, vertical
X_train = data[:split, :-1]
y_train = data[:split, -1].reshape( (-1, 1) )  # new shape: -1 rows, 1 col

X_test = data[split:, :-1]
y_test = data[split:, -1].reshape( (-1, 1) )

print( 'Number of examples in training set = % d' % (X_train.shape[0]) )
print( 'Number of examples in testing set = % d' % (X_test.shape[0]) )


# step 2 : linear regression using mini-batch gradient descent

# function to compute prediction
def hypothesis(X, tha): # theta is a vector , contains weight of x, weight of y, bias,
    return np.dot( X, tha )
# A Matrix 2x3 can dot B matrix 3x2, results is 2x2 matrix
# * or numspy.multiply will multiply  element at the same position, 2x3 * 2x3 = 2 x 3 matrix


# function to compute gradient of loss function
def gradient(X, y, theta):
    h = hypothesis( X, theta )
    grad = np.dot( X.transpose(), (h - y) ) # features' values *  loss
    return grad


# function to compute the loss for current value of theta.
def cost(X, y, theta):
    h = hypothesis( X, theta )
    J = np.dot( (h - y).transpose(), (h - y) ) # square loss  function : sum of distances between prediction and label
    J /= 2 # average distance
    return J[0]


# function to create a list containing mini-batches.
def create_mini_batches(X, y, batch_size):
    mini_batches = []
    data = np.hstack( (X, y) )
    np.random.shuffle( data )
    n_minibatches = data.shape[0] // batch_size
    i = 0

    for i in range( n_minibatches + 1 ):
        mini_batch = data[i * batch_size: (i + 1) * batch_size, :]
        X_mini = mini_batch[:, :-1]
        y_mini = mini_batch[:, -1].reshape( (-1, 1) )
        mini_batches.append( (X_mini, y_mini ))
        if data.shape[0] % batch_size != 0:
            mini_batch = data[i * batch_size: data.shape[0]]
            X_mini = mini_batch[:, :-1]
            y_mini = mini_batch[:, -1].reshape( (-1, 1) )
            mini_batches.append( (X_mini, y_mini) )

        return mini_batches


# function to perform mini-batch gradient descent

def gradientDescent(X, y, learning_rate=0.001, batch_size=32):
    theta = np.zeros( (X.shape[1], 1) ) # columns count = theta count
    error_list = []
    max_iter = 3
    for itr in range( max_iter ):
        mini_batches = create_mini_batches( X, y, batch_size )
        for mini_batch in mini_batches:
            X_mini, y_mini = mini_batch
            theta = theta - learning_rate * gradient( X_mini, y_mini, theta )
            error_list.append( cost( X_mini, y_mini, theta ) )

    return theta, error_list


theta, error_list = gradientDescent( X_train, y_train )
print( 'Bias = ', theta[0] )
print( 'Coefficients = ', theta[1:] )

# visualising gradient decent
plt.plot( error_list )
plt.xlabel( 'Number of iterations' )
plt.ylabel( 'Cost' )
plt.show()

# Step 3: make prediction on the testing set and compute the mean absolute error in the predictions.
# predicting output for X_test
y_pred = hypothesis( X_test, theta )
plt.scatter( X_test[:, 1], y_test[:, ], marker='.' )
plt.plot( X_test[:, 1], y_pred, color='orange' )
plt.show()

error = np.sum( np.abs( y_test - y_pred ) / y_test.shape[0] )
print( 'Mean absolute error = ', error )