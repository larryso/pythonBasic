import pandas as pd
import openpyxl


def pandas_excel_data_processing(input_file, output_file):
    ## read data from excel tp data_frame
    data_frame = pd.read_excel(input_file)
    print(data_frame)
    # Test1: 使用 iloc 从DataFrame中筛选数据
    # data.iloc[<row selection>, <column selection>]
    print(data_frame.iloc[0, 0])
    ## test 2: iloc 选择第一行
    print(data_frame.iloc[0])
    ## test3: iloc 选择最后一行
    print(data_frame.iloc[-1])
    ## test4 iloc 选择第一lie
    print(data_frame.iloc[:, 0])
    ## test5 选择数据中的最后一列
    print(data_frame.iloc[:, -1])
    ## test6 选择数据中的第 1-3 行的所有列
    print(data_frame.iloc[0:3])
    ## test7 选择数据中的前2列的所有行
    print(data_frame.iloc[:, 0:2])
    ## test8 选择第 0, 2, 4行 和 第 1,3 列
    print(data_frame.iloc[[0, 2, 4], [1, 3]])
    ## 选择第0-3行 的 0-2列
    print(data_frame.iloc[0:3, 0:2])
    '''
    使用iloc只选择了单独的一行或一列，返回的数据为 Series 类型，而如果选择了多行数据则会返回 DataFrame 类型，
    若只选择了一行，但需要要返回 DataFrame 类型，可以传入一个单值列表
    '''
    print(data_frame.iloc[[0]])
    print(data_frame.iloc[[1]])

    '''
    data.loc[<row selection>, <column selection>]
    ioc 用于以下两种场景：
      使用 下标 查找
      使用 条件 查找
    '''
    print(data_frame.loc[[1]])

    ## 选择第1到3行的 “Customer Name”、“Purchase Date” 列
    print(data_frame.loc[0:3, ["Customer Name", "Purchase Date"]])
    ## 使用逻辑判断选择数据
    ## 选择“Customer Name”列等于Tony1的 “Customer Name”列到 “Purchase Date” 列的数据
    print(data_frame.loc[data_frame['Customer Name'] == 'Tony', ['Customer Name', 'Purchase Date']])
    ## 选择 “产品名称”列 的值中是以 "【拍卖交易】" 开头的行的所有列

    if True:
        input_file = input_file.replace("test.xlsx", "数据爬取-金币涨跌追踪.xlsx")
        excel_date = pd.read_excel(input_file)
        print(excel_date)
        print('*' * 20)
        print(excel_date.loc[excel_date['产品名称'].str.startswith('【拍卖交易2】')])
        ## 选择 收购比例 = 69.01 并且 产品名称 是以 "【拍卖交易】"开头的行
        print(excel_date.loc[excel_date['产品名称'].str.startswith('【拍卖交易2】') & excel_date['收购比例'] == 69.01])
        ## 利用apply的lambda函数判断符合条件的行，如下选择 时间 列中20点的所有数据
        print(excel_date.loc[excel_date['日期'].apply(lambda x: x.split(' ')[1].split(':')[0] == '20')])
