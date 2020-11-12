import os.path
import xlrd
from mailmerge import MailMerge

docx = r'Template.docx'
xlsx = r'information.xlsx'


workbook = xlrd.open_workbook(xlsx)
worksheet = workbook.sheet_by_index(0)
nrow = worksheet.nrows
list1 = []  # 空列表

for key in range(1,nrow):
    dict_temp = {}  # 空字典
    dict_temp['yi'] = str(worksheet.cell_value(key, 5))
    dict_temp['ji'] = str(worksheet.cell_value(key, 6))
    dict_temp['d'] = str(worksheet.cell_value(key, 2))
    dict_temp['month'] = str(worksheet.cell_value(key, 3))
    dict_temp['jieri'] = str(worksheet.cell_value(key, 4))
    dict_temp['tiangan'] = str(worksheet.cell_value(key, 7))
    dict_temp['nongliyue'] = str(worksheet.cell_value(key, 8))
    dict_temp['nongli'] = str(worksheet.cell_value(key, 9))
    dict_temp['sen1'] = str(worksheet.cell_value(key, 10))
    dict_temp['sen2'] = str(worksheet.cell_value(key, 11))
    dict_temp['weekday'] = str(worksheet.cell_value(key, 12))
    dict_temp['gouzuori'] = str(worksheet.cell_value(key, 13))
    list1.append(dict_temp)

with MailMerge(docx) as doc:
    doc.merge_templates(list1, separator='page_break')
    output = r'C:\Users\admin\Desktop\output.docx'
    doc.write(output)
