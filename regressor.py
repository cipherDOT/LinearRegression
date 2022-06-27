
# For the learning of the regression model we are going to use the 
# principle of least squares. The task is to minimize the residual error.

# Mathematically, the intercept and slope of the regression line is given as,
#       slope    : cross_deviation_xy / squared_deviation_x
#       intecept : y_bar - slope * x_bar

class LinearRegression(object):
    def __init__(self, x_data, y_data):
        self.x = x_data
        self.y = y_data
        self.slope = 0
        self.intercept = 0

    # return the mean of a given list / vector
    def mean(self, data: list) -> float:
        return sum(data) / len(data)

    # multiply the elements of given two lists
    def multiply(self, x, y):
        resultant = []

        for i, j in zip(x, y):
            product = i * j
            resultant.append(product)

        return resultant

    # linear regression training
    def train(self):
        n = len(self.x)

        # finding the mean value of x and y datas
        x_mean = self.mean(self.x)
        y_mean = self.mean(self.y)

        # product of lists x and y
        xy_product = self.multiply(self.x, self.y)

        # square of list x (x * x)
        xx_product = self.multiply(self.x, self.x)

        # deviation of values in  y w.r.t values x
        cross_deviation_xy = sum(xy_product) - (n * x_mean * y_mean)

        # squared value of deviation of x
        squared_deviation_x = sum(xx_product) - (n * x_mean * x_mean)

        # slope and intercept as per the equation
        slope = cross_deviation_xy / squared_deviation_x
        intercept = y_mean - slope * x_mean

        # re-assigning the object "data variables"
        self.slope = slope
        self.intercept = intercept

    # prediction function
    def predict(self, x):
        y = self.intercept + (self.slope * x)
        return y

    # print out the statistics i.e., slope and intercept
    def stats(self):
        print(f'slope     : ', self.slope)
        print(f'intercept : ', self.intercept)
