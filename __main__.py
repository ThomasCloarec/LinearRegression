import matplotlib.pyplot as plt
import csv
import random
import math


def main():
    plt.ion()

    # Defining default plot
    plt.axis([0, 100, 0, 100])

    # Import dataset
    dataset = import_csv_data('train.csv')

    # Scatter plot
    for data_tuple in dataset:
        plt.scatter(data_tuple[0], data_tuple[1])

    for i in range(0, 1000):
        plt.pause(0.05)
        b = random.randint(0, 100)
        a = math.tan(random.uniform(-math.pi / 2, math.pi / 2))
        plt.plot([0, 100], [b, a * 100 + b])


def import_csv_data(filename):
    dataset = []

    with open(filename, 'rt') as f:
        dataset_reader = csv.reader(f)
        i = 0

        for data_row in dataset_reader:
            row = [float(data) for data in data_row]
            print(row)
            dataset.append(row)
            i += 1

    return dataset


if __name__ == "__main__":
    main()
