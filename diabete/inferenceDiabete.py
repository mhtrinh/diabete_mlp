
import argparse

from . import diabete
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Run inference (aka prediction) from trained model")
    parser.add_argument("model",help="Path to trained model.")
    parser.add_argument("input",help="Path to the input csv to run prediction against. The csv can have one or more rows. The column order must be the same as the one used to train the model (and excluding the last target column)")

    args = parser.parse_args()


    diabete.inference(args.input,args.model)

if __name__ == "__main__":
    main()