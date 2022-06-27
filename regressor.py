
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

    def mean(self, data: list) -> float:
        return sum(data) / len(data)

    def multiply(self, x, y):
        resultant = []

        for i, j in zip(x, y):
            product = i * j
            resultant.append(product)

        return resultant

    def train(self):
        n = len(self.x)

        x_mean = self.mean(self.x)
        y_mean = self.mean(self.y)

        xy_product = self.multiply(self.x, self.y)
        xx_product = self.multiply(self.x, self.x)

        cross_deviation_xy = sum(xy_product) - (n * x_mean * y_mean)
        squared_deviation_x = sum(xx_product) - (n * x_mean * x_mean)

        slope = cross_deviation_xy / squared_deviation_x
        intercept = y_mean - slope * x_mean

        self.slope = slope
        self.intercept = intercept

    def predict(self, x):
        y = self.intercept + (self.slope * x)
        return y

    def stats(self):
        print(f'slope     : ', self.slope)
        print(f'intercept : ', self.intercept)
