import sys
import os


def csv_simple_read_write(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8', newline='') as file_reader:
            with open(output_path, 'w', encoding='utf-8', newline='') as file_writer:
                header = file_reader.readline().strip() ## readline() methad read the first line of the file
                header_list = header.split(",")
                print(header_list)
                file_writer.write(','.join(map(str, header_list))+'\n')
                for row in file_reader:
                    row = row.strip()
                    row_list = row.split(",")
                    print(row_list)
                    file_writer.write(','.join(map(str, row_list))+'\n')
    except IOError:
        print("File Not Found!!")


