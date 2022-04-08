import pandas as pd
import sys
import os
import glob
import openpyxl


def excel_data_processing(input_path, output_file):
    ## sum and average per workbook and shee
    all_workbooks = glob.glob(os.path.join(input_path, '*.xls*'))
    data_frames = []

    for workbook in all_workbooks:
        print(workbook)
        worksheet_data_frames = []
        all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
        for work_sheet_name, data in all_worksheets.items():
            # total_ammount = pd.DataFrame([float(str(value).strip('s').replace(',',''))
            #                               for value in data.loc[:,'收购金额RMB']]).sum()
            if data.empty:
                continue
            total_ammount = data.fillna(0).loc[:, '收购金额RMB'].sum()
            total_quality = data.fillna(0).loc[:, '收购金币数量'].sum()
            average = total_ammount / total_quality
            data = {'workbook': [os.path.basename(workbook)],
                    'worksheet': [work_sheet_name],
                    'worksheet_total': [total_ammount],
                    'worksheet_quality': [total_quality],
                    'worksheet_average': [average]}
            worksheet_data_frames.append(pd.DataFrame(data))
        worksheets_data_frame = pd.concat(worksheet_data_frames, axis=0, ignore_index=True) ## 将两个data_frame 合并
        print(worksheets_data_frame)
        workbook_total = worksheets_data_frame.loc[:,'worksheet_total'].sum()
        workbook_quality = worksheets_data_frame.loc[:,'worksheet_quality'].sum()
        workbook_average = workbook_total / workbook_quality
        workbook_stats = {'workbook': [os.path.basename(workbook)],
                          'workbook_total':[workbook_total],
                          'workbook_quality': [workbook_quality],
                          'workbook_average': [workbook_average]}

        workbook_stats = pd.DataFrame(workbook_stats)
        workbook_data_frame = pd.merge(worksheets_data_frame, workbook_stats, on='workbook', how='left')
        print(workbook_data_frame)
        data_frames.append(workbook_data_frame)
    all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True) ## axis=0 使用0值表示沿着每一列或行标签/索引值向下执行方法
    # print(all_data_concatenated)


