import pandas as pd
import statistics
## import numpy as np ##

def loadData(filename):
    frame = pd.read_csv(filename, header=None)
    return frame

def calculate_statistics(frame):
    mean = frame.mean()
    median = frame.median()
    mode = statistics.mode(frame[0])  # statistics.mode() requires a 1D list, so we use frame[0]
    maximum = frame.max()
    minimum = frame.min()
    quartile_25 = frame.quantile(0.25)
    quartile_75 = frame.quantile(0.75)

    return mean, median, mode, maximum, minimum, quartile_25, quartile_75

def main():
    frame = loadData("1000_Random_Numbers.csv")
    mean, median, mode, maximum, minimum, quartile_25, quartile_75 = calculate_statistics(frame)

    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("25% Quartile:", quartile_25)
    print("75% Quartile:", quartile_75)

main()
