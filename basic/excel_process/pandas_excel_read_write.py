import pandas as pd
import sys

import openpyxl

def pandas_excel_read_write(input_file, output_file):
    data_frame = pd.read_excel(input_file, sheet_name='january_2022')
    print(data_frame)
    writer = pd.ExcelWriter(output_file)
    data_frame.to_excel(writer, sheet_name='january_2022_output', index=True)
    writer.save()
