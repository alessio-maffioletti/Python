import sys
import torch
import torch.nn as nn 
import matplotlib.pyplot as plt
import random
import mnist_data
import nn as nrlNetwrk


class agent():
    def __init__(self, network, epochs=3000, lr=0.3):
        self.epochs = epochs
        self.lr = lr
        self.network = network

    def get_corresponding_digit(self, tensor):
        max_index = torch.argmax(tensor)
        digit = max_index.item()
        return digit


    def visualize_output(self, image, prediction, label):
        image_np = image.numpy().reshape(28, 28)

        # Display the image using matplotlib
        plt.imshow(image_np, cmap='gray')
        plt.title((f"prediction: {prediction} label:{label}"))
        plt.show()


    def use_nn(self, network, test_data_x, test_data_y):

        rand_index = random.randint(0, len(test_data_x))

        prediction_raw = network.forward(test_data_x[rand_index])
        prediction = self.get_corresponding_digit(prediction_raw)
        self.visualize_output(test_data_x[rand_index], prediction, test_data_y[rand_index].detach().numpy())



    def train(self, input, labels):
        grad_function = torch.optim.SGD(self.network.parameters(), lr=self.lr)
        loss_function = nn.CrossEntropyLoss()


        for epoch in range(self.epochs):
            prediction = self.network.forward(input)

            loss = loss_function(prediction, labels)

            grad_function.zero_grad()
            loss.backward()
            grad_function.step()

            if epoch % 500 == 0:
                print(f"loss: {round(loss.item(), 4)}")

def main():
    nn_h1_Size = 16
    nn_h2_Size = 16

    epochs = 2000
    learning_rate = 0.3

    testing_loop = 5


    datalib = mnist_data.MNISTData()
    train_dt_x, train_dt_y = datalib.create_data(True)
    test_dt_x, test_dt_y = datalib.create_data(False)

    network = nrlNetwrk.NeuralNetwork(nn_h1_Size,nn_h2_Size)
    my_agent = agent(network, epochs, learning_rate)


    my_agent.train(train_dt_x, train_dt_y)
    for _ in range(testing_loop):
        my_agent.use_nn(network, test_dt_x, test_dt_y)


if __name__ == "__main__":
    sys.exit(main())