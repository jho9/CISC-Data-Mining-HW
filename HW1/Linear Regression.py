# James Ho
# CISC:Data Mining
# HW#1

#Normal Equation to calculate beta values
def get_betas(X,y):
    m = int(X.shape[0])
    beta = []
    bias_vector = np.ones((m,1))
    X = np.reshape(X, (m,1))
    X = np.append(bias_vector, X, axis = 1)
    X_t = X.transpose()
    betas = pinv(X_t.dot(X)).dot(X_t).dot(y)
    return betas

#Calculates predictions given a X matrix and Beta vectors
def calc_prediction(x_test, betas):
    m = int(x_test.shape[0])
    bias_vector = np.ones((m,1))
    x_test = np.reshape(x_test, (m,1))
    x_test = np.append(bias_vector, x_test, axis = 1)
    return x_test.dot(betas)
    
def squared_error_rate(predicted_y_test, y_test):
    se = predicted_y_test - y_test
    se = se**2
    se = sum(se)
    return se/y_test.size
 
