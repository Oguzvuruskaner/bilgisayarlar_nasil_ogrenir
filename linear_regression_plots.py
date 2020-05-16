import numpy as np
import matplotlib.pyplot as plt


def get_random_data() -> (np.array,np.array):

    x = np.random.uniform(-10,10,(100,1))
    y = 2*x + 4 + np.random.normal(scale=.5,size=(100,1))

    return x,y

def plot_only_data(x,y):

    plt.scatter(x,y,s=10)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Elimizdeki Veri")
    plt.savefig("sade_cizim.png")
    plt.clf()

def plot_with_prediction(x,y,x_predicted,y_predicted,plt_title):

    plt.scatter(x,y,s=10)
    plt.plot(x_predicted,y_predicted)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(plt_title)
    plt.savefig("{}.png".format(plt_title))
    plt.clf()


if __name__ == "__main__":

    x,y = get_random_data()

    plot_only_data(x,y)
    
    x_predicted = np.arange(-10,10,.01)
    y_predicted = x_predicted**2
    plot_with_prediction(x,y,x_predicted,y_predicted,"X^2")


    x_predicted = np.arange(-10,10,.01)
    y_predicted = x_predicted
    plot_with_prediction(x,y,x_predicted,y_predicted,"x")

    x_predicted = np.arange(-10,10,.01)
    y_predicted = 2*x_predicted
    plot_with_prediction(x,y,x_predicted,y_predicted,"2x")

    x_predicted = np.arange(-10,10,.01)
    y_predicted = 2*x_predicted+4
    plot_with_prediction(x,y,x_predicted,y_predicted,"2x+4")