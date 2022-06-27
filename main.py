from regressor import LinearRegression
from netutils import graph

if __name__ == "__main__":
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [1, 2, 4, 7, 8, 9, 13, 16, 19, 20]

    regress = LinearRegression(x, y)
    regress.train()
    regress.stats()
    
    graph(x, y, regress)
