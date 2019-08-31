import matplotlib.pyplot as plt
import csv


def main():
    # Defining default plot
    plt.axis([0, 160, 0, 160])
    plt.xlabel('Size (m²)')
    plt.ylabel('Price (€)')
    plt.title('[Apartment] f(size) = price')

    # Initialize the default dataset
    dataset = Dataset()
    # Scatter plot
    plt.plot(dataset.get_x(), dataset.get_y(), color='b', marker='x', ls='', ms=10)

    plt.show()


class Dataset:
    def __init__(self):
        self.dataset_reader = CSVReader('dataset.csv')

    def get_x(self):
        return self.dataset_reader.get_row(0)

    def get_y(self):
        return self.dataset_reader.get_row(1)


class CSVReader:
    def __init__(self, filename):
        self.filename = filename

    def get_row(self, row_index):
        with open(self.filename, 'rt') as f:
            dataset = csv.reader(f)
            i = 0
            for data_row in dataset:
                if i == row_index:
                    row = [int(data) for data in data_row]
                    return row
                i += 1


if __name__ == "__main__":
    main()
