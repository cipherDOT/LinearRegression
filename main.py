
# importing the model class and the utility functions
from regressor import LinearRegression
from netutils import graph

# main process
if __name__ == "__main__":

    # x and y data
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [1, 2, 4, 7, 8, 9, 13, 16, 19, 20]

    # linear regression model object instance
    regress = LinearRegression(x, y)

    # training phase
    regress.train()

    # print out the slope and intercept of the regression line
    regress.stats()
    
    # plot the regression graph
    graph(x, y, regress)
