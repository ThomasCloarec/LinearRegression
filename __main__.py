from matplotlib import pyplot as plt
import csv
import random
import math
import time


def main():
    train()


def train(dataset_filename="train.csv", epoch=500, learning_rate_a=0.0001, learning_rate_b=0.1
          , plot_update_interval=0.2, a=math.tan(random.uniform(-math.pi / 2, math.pi / 2)),
          b=random.randint(0, 100)
          ):
    # Import dataset
    dataset = import_csv_data(dataset_filename)

    # Enable plot animation
    plt.ion()

    # Define default plot
    plt.axis([0, 100, 0, 100])

    # Draw data points
    for data_point in dataset:
        plt.scatter(data_point[0], data_point[1])

    # Initialize loop parameters
    hypothesis_line = None
    hypothesis_text = None
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
            hypothesis_line, = plt.plot([0, 100], [b, a * 100 + b])

            # Update hypothesis text
            if hypothesis_text is not None:
                hypothesis_text.remove()
            hypothesis_text = plt.text(10, 80,
                                       "f(x) = " + str(math.ceil(a * 1000) / 1000) + "x + " + str(
                                           math.ceil(b * 1000) / 1000))

            #  Update plot
            plt.pause(0.0001)

        # Define cost
        cost_a = 0
        cost_b = 0
        for sample in dataset:
            temp_hypothesis = a * sample[0] + b
            cost_a = cost_a + ((temp_hypothesis - sample[1]) * sample[0]) / len(dataset)
            cost_b = cost_b + (temp_hypothesis - sample[1]) / len(dataset)

        # Update parameters
        a -= learning_rate_a * cost_a
        b -= learning_rate_b * cost_b

    # Last update for hypothesis line
    if hypothesis_line is not None:
        hypothesis_line.remove()
    hypothesis_line, = plt.plot([0, 100], [b, a * 100 + b])

    # Last update for hypothesis text
    if hypothesis_text is not None:
        hypothesis_text.remove()
    hypothesis_text = plt.text(10, 80,
                               "f(x) = " + str(math.ceil(a * 1000) / 1000) + "x + " + str(math.ceil(b * 1000) / 1000))

    # Calculate the final duration of the execution
    duration = time.time() - begin

    # Draw the final duration time text
    plt.text(10, 70, "execution duration : " + str(math.ceil(duration * 1000) / 1000) + "s")

    # Update the plot for the last time and keep it open for an hour
    plt.pause(3600)


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
