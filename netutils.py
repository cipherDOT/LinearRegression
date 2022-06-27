from matplotlib import pyplot as plt

def graph(x, y, model):
    predictions = [model.predict(i) for i in x]
    plt.scatter(x, y, color = "m",marker = "o", s = 30)
    plt.plot(x, predictions, color='b')
    plt.show()
