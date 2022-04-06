import sys
import pandas as pd

def csv_pandas_read_write(input_file, output_file):
    try:
        data_frame = pd.read_csv(input_file)
        print(data_frame)
        data_frame.to_csv(output_file)
    except IOError:
        print("Error read and Write files!!")