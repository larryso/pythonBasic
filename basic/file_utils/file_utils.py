import os
import glob


def dir_travel(file_path):
    if os.path.exists(file_path):
        file_sum = 0
        dir_sum = 0
        for root, dirs, files in os.walk(file_path):
            for file in files:
                abs_file_path = os.path.join(file_path, file)
                print("file path: %s" % (abs_file_path))
                file_sum += 1
            for dir in dirs:
                abs_dir = os.path.join(file_path, dir)
                print("abs dir path is: %s" % (abs_dir))
                dir_sum += 1

        return file_sum, dir_sum

    else:
        print("File path not exists!!")
        return False


def append_write2file(file_path, file_name, message):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    # file = open(os.path.join(file_path,file_name), "a")
    with open(os.path.join(file_path, file_name), "a") as file:
        file.write(message)


def read_multiple_txt(file_path):
    print(file_path)
    for input_file in glob.glob(os.path.join(file_path, '*.txt')):
        with open(input_file, 'r', encoding='utf-8', newline='') as file_reader:
            for row in file_reader:
                print(row)
