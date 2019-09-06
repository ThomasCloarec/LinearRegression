import matplotlib.pyplot as plt
import csv
import random
import math


def main():
    # Define learning rate and epoch
    learning_rate_a = 0.0001
    learning_rate_b = 0.1
    epoch = 500

    # Import dataset
    dataset = import_csv_data('train.csv')

    # Initialize random parameters
    a = math.tan(random.uniform(-math.pi / 2, math.pi / 2))
    b = random.randint(0, 100)

    # Enable plot animation
    plt.ion()

    # Draw data points
    for data_point in dataset:
        plt.scatter(data_point[0], data_point[1])

    for i in range(0, epoch):
        # Define default plot
        plt.axis([0, 100, 0, 100])

        # Draw hypothesis
        ln, = plt.plot([0, 100], [b, a * 100 + b])

        # Define cost
        cost_a = 0
        cost_b = 0
        for sample in dataset:
            temp_hypothesis = a * sample[0] + b
            cost_a = cost_a + (temp_hypothesis - sample[1]) * sample[0]
            cost_b += temp_hypothesis - sample[1]
        cost_a /= len(dataset)
        cost_b /= len(dataset)

        # Update parameters
        a -= learning_rate_a * cost_a
        b -= learning_rate_b * cost_b

        #  Wait before next hypothesis
        plt.pause(0.01)

        # Remove last hypothesis
        ln.remove()

    # Prevent program from ending
    print()


# Import and transform an CSV file into a list
def import_csv_data(filename):
    dataset = []

    with open(filename, 'rt') as f:
        dataset_reader = csv.reader(f)
        i = 0

        for data_row in dataset_reader:
            row = [float(data) for data in data_row]
            dataset.append(row)
            i += 1

    return dataset


if __name__ == "__main__":
    main()
