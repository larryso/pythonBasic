import sys
from xlrd import open_workbook
from xlwt import Workbook

def excel_read_write(input_file, output_file):
    output_workbook = Workbook()
    output_worksheet = output_workbook.add_sheet('january_2022_output')
    with open_workbook(input_file) as workbook:
        worksheet = workbook.sheet_by_name('january_2022')
        for row_index in range(worksheet.nrows):
            for colum_index in range(worksheet.ncols):
                print(worksheet.cell_value(row_index, colum_index))
                output_worksheet.write(row_index, colum_index, \
                                       worksheet.cell_value(row_index, colum_index))
    output_workbook.save(output_file)