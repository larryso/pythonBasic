import pandas as pd
import openpyxl
import numpy as np


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

    if False:
        input_file = input_file.replace("test.xlsx", "数据爬取-金币涨跌追踪.xlsx")
        excel_date = pd.read_excel(input_file)
        print(excel_date)
        print('*' * 20)
        print(excel_date.loc[excel_date['产品名称'].str.startswith('【拍卖交易2】')])
        ## 选择 收购比例 = 69.01 并且 产品名称 是以 "【拍卖交易】"开头的行
        print(excel_date.loc[excel_date['产品名称'].str.startswith('【拍卖交易2】') & excel_date['收购比例'] == 69.01])
        ## 利用apply的lambda函数判断符合条件的行，如下选择 时间 列中20点的所有数据
        print(excel_date.loc[excel_date['日期'].apply(lambda x: x.split(' ')[1].split(':')[0] == '20')])

        ## 写 Excel 文件
        ## 筛选
        idx = excel_date['日期'].apply(lambda x: x.split(" ")[1].split(':')[0] == '20')

        output_data = excel_date.loc[idx, ['产品名称', '收购比例']]
        print(output_data)
        output_data.to_excel(output_file, index=False)

        ## 写多个sheet
        sheet_dict = {}
        data1 = excel_date.loc[idx, ['日期','产品名称']]
        sheet_dict['data1'] = data1

        data2 = excel_date.loc[idx, ['产品名称', '收购比例']]
        sheet_dict['data2'] = data2
        writer = pd.ExcelWriter(output_file)
        for sheet_name, sheet_data in sheet_dict.items():
            sheet_data.to_excel(writer, sheet_name, index=False)
        writer.save()

def data_frame_test(input_file):
    ## create empty dataFrame
    data_frame = pd.DataFrame(columns={'c1', 'c2', 'c3'}, index=[0])
    print(data_frame)
    ## data_frame.describe()
    data_frame = pd.read_excel(input_file)
    print(data_frame.describe())
    print(data_frame.head())
    print(data_frame.tail())
    print(data_frame)
    ## 单独计算某列的统计值
    print(data_frame['收购金额RMB'].sum())
    #mean–>平均数
    print(data_frame['收购金额RMB'].mean())
    print(data_frame['收购金额RMB'].count())
    print(data_frame['收购金额RMB'].max())
    ## 查看dataframe的数据数目：
    print(data_frame.size)
    ## 返回列数：
    print(data_frame.ndim)
    print(data_frame.axes)
    ## 缺失值可以删除也可以用均值或者0等数填充：
    print(data_frame.fillna(0))
    print(data_frame.dropna())
    ## 去除有NaN值的行或列(axis=0去除行，=1去除列)：
    print(data_frame.dropna(axis=0))
    print(data_frame.dropna(axis=1))

    ## test merge
    df1 = pd.DataFrame({'key': ['one', 'two', 'two'],
                        'data1': np.arange(3)})
    df2 = pd.DataFrame({'key': ['one', 'three', 'three'],
                        'data2': np.arange(3)})
    ## 默认：以重叠的列名当作连接键, 默认how 为 innner （交集）
    df3 = pd.merge(df1,df2)
    df4 = pd.merge(df1, df2, how='left')
    df5 = pd.merge(df1,df2, how='right')
    df6 = pd.merge(df1, df2, how='outer')
    print(df1)
    print(df2)
    print(df3)
    print(df4)
    print(df5)
    print(df6)
    ## 多键连接时将连接键做成列表传入。on默认是两者同时存在的列
    df7 = pd.DataFrame({'key': ['one', 'two', 'two'],
                        'value': ['a','b','c'],
                        'data1': np.arange(3)})
    df8 = pd.DataFrame({'key': ['one', 'three', 'three'],
                        'value': ['a', 'b', 'c'],
                        'data2': np.arange(3)})
    df9 = pd.merge(df7,df8, on=['key', 'value'], how='left')
    print(df9)
    df10 = pd.merge(df7, df8, left_on=['key', 'data1'], right_on=['key', 'data2'], how='left', indicator=True)
    print(df10)


