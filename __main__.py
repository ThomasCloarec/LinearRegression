from matplotlib import pyplot as plt
import csv
import random
import math
import time


def main():
    model = Model()
    model.train(dataset_filename="train.csv")
    model.test(dataset_filename="test.csv")


class Model:
    def __init__(self, a=math.tan(random.uniform(-math.pi / 2, math.pi / 2)), b=random.randint(0, 100)):
        self.a = a
        self.b = b

    def train(self, dataset_filename="train.csv", epoch=1000, learning_rate_a=0.0001, learning_rate_b=0.1,
              plot_update_interval=0.22):
        # Import dataset
        dataset = import_csv_data(dataset_filename)

        # Prepare plot
        prepare_plot("Training model on \"" + dataset_filename + "\"")

        # Draw data points
        for data_point in dataset:
            plt.scatter(data_point[0], data_point[1])

        # Draw learning parameters and plot update interval
        plt.text(55, 25, "learning rate A = " + str(learning_rate_a))
        plt.text(55, 15, "learning rate B = " + str(learning_rate_b))
        plt.text(55, 5, "plot update interval = " + str(plot_update_interval) + "s")

        # Initialize loop parameters
        hypothesis_line = None
        hypothesis_text = None
        epoch_text = plt.text(55, 35, "epoch = 0/" + str(epoch) + " (0%)")
        last_update_plot_time = 0
        begin = time.time()

        # Linear regression loop using stochastic gradient descent
        for i in range(0, epoch):
            if last_update_plot_time == 0 or time.time() > last_update_plot_time + plot_update_interval:
                # Update last update time
                last_update_plot_time = time.time()

                # Update hypothesis line
                if hypothesis_line is not None:
                    hypothesis_line.remove()
                hypothesis_line, = plt.plot([0, 100], [self.b, self.a * 100 + self.b])

                # Update hypothesis text
                if hypothesis_text is not None:
                    hypothesis_text.remove()
                hypothesis_text = plt.text(10, 90,
                                           "f(x) = " + str(math.ceil(self.a * 1000) / 1000) + "x + " + str(
                                               math.ceil(self.b * 1000) / 1000))

                # Update epoch text
                if epoch_text is not None:
                    epoch_text.remove()
                epoch_text = plt.text(55, 35,
                                      "epoch = " + str(i) + "/" + str(epoch) + " (" + str(
                                          math.ceil(i / epoch * 100)) + "%)")

                #  Update plot
                plt.pause(0.0001)

            # Define cost
            cost_a = 0
            cost_b = 0
            for sample in dataset:
                temp_hypothesis = self.a * sample[0] + self.b
                cost_a = cost_a + ((temp_hypothesis - sample[1]) * sample[0]) / len(dataset)
                cost_b = cost_b + (temp_hypothesis - sample[1]) / len(dataset)

            # Update parameters
            self.a -= learning_rate_a * cost_a
            self.b -= learning_rate_b * cost_b

        # Last update for hypothesis line
        if hypothesis_line is not None:
            hypothesis_line.remove()
        hypothesis_line, = plt.plot([0, 100], [self.b, self.a * 100 + self.b])

        # Last update for hypothesis text
        if hypothesis_text is not None:
            hypothesis_text.remove()
        hypothesis_text = plt.text(10, 90,
                                   "f(x) = " + str(math.ceil(self.a * 1000) / 1000) + "x + " + str(
                                       math.ceil(self.b * 1000) / 1000))

        # Last update for epoch text
        if epoch_text is not None:
            epoch_text.remove()
        epoch_text = plt.text(55, 35,
                              "epoch = " + str(epoch) + "/" + str(epoch) + " (100%)")

        # Define and draw final cost
        cost = 0
        for sample in dataset:
            temp_hypothesis = self.a * sample[0] + self.b
            cost = cost + (temp_hypothesis - sample[1]) / len(dataset)
        plt.text(10, 80, "cost = " + str(math.ceil(cost * 1000) / 1000))

        # Draw execution duration time
        duration = time.time() - begin
        plt.text(10, 70, "execution duration : " + str(math.ceil(duration * 1000) / 1000) + "s")

        # Update the plot for the last time and keep it open for 5 seconds
        plt.pause(5)

    def test(self, dataset_filename="test.csv"):
        # Import dataset
        dataset = import_csv_data(dataset_filename)

        # Prepare plot
        prepare_plot("Testing model on \"" + dataset_filename + "\"")

        # Draw data points
        for data_point in dataset:
            plt.scatter(data_point[0], data_point[1])

        # Draw hypothesis line
        hypothesis_line, = plt.plot([0, 100], [self.b, self.a * 100 + self.b])

        # Draw hypothesis text
        hypothesis_text = plt.text(10, 90,
                                   "f(x) = " + str(math.ceil(self.a * 1000) / 1000) + "x + " + str(
                                       math.ceil(self.b * 1000) / 1000))

        # Define and draw cost
        cost = 0
        for sample in dataset:
            temp_hypothesis = self.a * sample[0] + self.b
            cost = cost + (temp_hypothesis - sample[1]) / len(dataset)

        # Draw the final duration time text
        plt.text(10, 80, "cost = " + str(math.ceil(cost * 1000) / 1000))

        # Update the plot for the last time and keep it open for 10 seconds
        plt.pause(10)


def prepare_plot(title="Linear regression model", x1=0, x2=100, y1=0, y2=100):
    # Clean plot
    plt.clf()

    # Define title
    plt.title(title)

    # Enable plot animation
    plt.ion()

    # Define default plot
    plt.axis([x1, x2, y1, y2])


# Import and transform an CSV file into a list
def import_csv_data(filename):
    dataset = []

    with open(filename, 'rt') as f:
        dataset_reader = csv.reader(f)
        i = 0

        # Use the dataset reader (a csv reader) to fill an usable dataset
        for data_row in dataset_reader:
            row = [float(data) for data in data_row]
            dataset.append(row)
            i += 1

    return dataset


if __name__ == "__main__":
    main()
