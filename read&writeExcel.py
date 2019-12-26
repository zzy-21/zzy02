import xlrd
wb=xlrd.open_workbook(r'/Users/zhaozhenyu/zzy/test.xlsx')
# 方法1:读取每个sheet每一行数据，将每一行数据放入一个列表中，去列表倒数第一个元素
for s in wb.sheets():
    print('the last column of sheet %s:'%(s.name))
    for i in range(s.nrows):
        print(s.row(i)[-1].value)
# 方法2：
for i in range(wb.nsheets):
    s=wb.sheet_by_index(i)
    print('the last column of sheet %s:'%(s.name))
    for v in s.col_values(s.ncols-1):
        print(v)
# 方法3
for name in wb.sheet_names():
    print('the last column of sheet %s:'%(name))
    s=wb.sheet_by_name(name)
    c=s.ncols-1
    for r in range(s.nrows):
        print(s.cell_value(r,c))
import xlwt
book= xlwt.Workbook(encoding='utf-8')
sheet=book.add_sheet('sheet_test',cell_overwrite_ok=True)
sheet.write(0,0,'mike')
sheet.row(0).write(1,'&')
sheet.write(0,2,'jack')
sheet.col(2).width=300
book.save(r'/Users/zhaozhenyu/zzy/test1.xls')
