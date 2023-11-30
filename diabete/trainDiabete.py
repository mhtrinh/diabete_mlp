#!/usr/bin/env python3

import argparse

from . import diabete

def main():
    parser = argparse.ArgumentParser(description="Train model using csv")
    parser.add_argument("data",help="Csv file used to train the model. The last column is used as target.")
    parser.add_argument("output",help="Path to file to witch the model will be saved.")
    parser.add_argument("--testSize",default=0.1, help="Ratio of data to be used as split. Default: %(default)f")
    parser.add_argument("-q","--quiet",default=False, help="Quiet mode. Do not show stats. Default: False")
    parser.add_argument("--layer",default="(10,10,10)", help="Define the sizes of hidden layers of the MLP. Default: %(default)s")
    args = parser.parse_args()
    diabete.train(csv_path=args.data,
                  trained_model_path=args.output,
                  test_size=args.testSize,
                  verbose=not args.quiet,
                  hidden_layer=eval(args.layer))

if __name__ == "__main__":
    main()





