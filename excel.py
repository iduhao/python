#author duhao
import xlrd
import xlwt

#简单的一个程序，使用xlrd和xlwt模块，创建一个excel表格，并且获取创建的表格的sheet名字
#创建excel表格只能支持xls文件
new_wb = input("Please input workbook name:")
new_sheet =input("Please input sheet_name:")
wb = xlwt.Workbook()
ws = wb.add_sheet(new_sheet)
wb.save(new_wb + '.xls')



#读取excel表格
xlsx = xlrd.open_workbook(new_wb + '.xls')
table = xlsx.sheet_by_index(0)
sheet_name = xlsx.sheet_names()
print(sheet_name)
# value = table.cell_value(2,1) 
# print (value)
#获取表格的行数
# nrows = table.nrows
# print(nrows)
# #获取单个单元格的值
# value = table.cell_value(2,1)
# print(value)