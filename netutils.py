
# import the visualization library (matplotlib in this case)
from matplotlib import pyplot as plt

# applying dark background
plt.style.use('dark_background')

def graph(x, y, model):

    # get predictions of all data
    predictions = [model.predict(i) for i in x]

    # plot code
    plt.scatter(x, y, color = "m",marker = "o", s = 30)
    plt.plot(x, predictions, color='b')
    plt.show()
