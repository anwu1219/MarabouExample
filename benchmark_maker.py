import warnings
warnings.filterwarnings('ignore')
from keras.datasets import mnist
import os
import numpy as np
import sys
import argparse

def parse_args():
    p = argparse.ArgumentParser()
    # options
    p.add_argument('-e', '--epsilon', required=False, type=float, default=0.01,
                   help='Epislon value')
    p.add_argument('-o', '--original-label', required=True, type=int, help="Correct label")
    p.add_argument('-t', '--target-label', required=True, type=int,
                   help='Targeted label')
    p.add_argument('-f', "--filename", default="robustness", help="The prefix of the generated property files")
    p.add_argument('-d', '--dump-directory', default="./", help = 'The directory to dump the property file')
    p.add_argument('-n', '--number-of-properties', type=int, default=1, help="Number of properties to dump")
    p.add_argument("-s", "--seed", default=0, type=int, help="random seed for getting training point")
    # parse arguments
    opts = p.parse_args()
    return opts


def dumpMNISTTargetedAttackPropertyFile(X, epsilon, target, filename):
    # target: 0..9 corresponding to y0..y9
    with open(filename, 'w') as out_file:
        X = np.array(X).flatten() / 255 # Normalize each input to between 0 and 1
        for i, x in enumerate(X):
            out_file.write('x{} >= {}\n'.format(i, x - epsilon))
            out_file.write('x{} <= {}\n'.format(i, x + epsilon))
        for i in range(10):
            if i != target:
                out_file.write('+y{} -y{} <= 0\n'.format(i, target))

def main():
    opts = parse_args()
    eps = opts.epsilon
    original = opts.original_label
    target = opts.target_label
    dump_directory = opts.dump_directory
    filenamePrefix = opts.filename
    number_of_properties = opts.number_of_properties
    seed = opts.seed

    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    label_to_points = {} # group label to training point indices
    for i, label in enumerate(y_train):
        if label not in label_to_points:
            label_to_points[label] = []
        label_to_points[label].append(i)

    # choose n input points that has the specified correct label
    np.random.seed(seed)
    points = np.random.choice(label_to_points[original], size=number_of_properties, replace=False)

    for index in points:
        property_filename = os.path.join(dump_directory, "{}_tar{}_eps{}_ind{}.txt".format(filenamePrefix, target, eps, index))
        dumpMNISTTargetedAttackPropertyFile(X_train[index], eps, target, property_filename)

if __name__ == "__main__":
    main()
