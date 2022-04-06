import pandas as pd
import openpyxl

def pandas_excel_data_processiong(input_file, output_file):
    ## read data from excel tp data_frame
    data_frame = pd.read_excel(input_file)
    print(data_frame)