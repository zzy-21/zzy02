import xlrd
'''
1.导入读取Excel包xlrd包
2.打开目标文件
3.定位sheet
4.定位行和列
5.读取数据
6.组装数据
7.return数据给需要数据的地方
'''
class getExcelData(object):
    def __init__(self):
        # 打开excel文件
        self.readbook = xlrd.open_workbook(r'/Users/zhaozhenyu/Downloads/data.xls')
        print(self.readbook)
        # 获取读入的文件sheet
        self.urlsheet=self.readbook.sheet_by_name('urlSheet')
        self.urlNum=self.urlsheet.nrows
        self.paramsheet=self.readbook.sheet_by_name('paramSheet')
        self.paramNum=self.paramsheet.nrows
        self.assertsheet=self.readbook.sheet_by_name('assertSheet')
        self.assertNum=self.assertsheet.nrows
# 定位行和列
    def getSheetData(self,num,sheetName):
        data=[]
        # 循环条件
        for i in range(1,num):
            # 循环体
            sheetData=sheetName.row_values(i)
            data.append(sheetData)
        return data
#组装数据
    def assembData(self):
        # 组装数据，把每个sheet页中id相同的组装在一起
        self.urlsheetList = self.getSheetData(self.urlNum, self.urlsheet)
        # print('urlsheet页数据', self.urlsheetList)
        self.paramsheetList = self.getSheetData(self.paramNum, self.paramsheet)
        # print('paramsheetData页数据', self.paramsheetList)
        self.assertsheetList = self.getSheetData(self.assertNum, self.assertsheet)
        # print('assertsheetData', self.assertsheetList)
        new_data = []
        for j in range(len(self.urlsheetList)):
            urlsheet_value = self.urlsheetList[j]
            paramsheet_value = self.paramsheetList[j][1:]
            urlsheet_value.append(paramsheet_value)
            assertsheet_value = self.assertsheetList[j][1:]
            urlsheet_value.append(assertsheet_value)
            print(urlsheet_value)
            new_data.append(urlsheet_value)
            # print('组装数据为：',new_data)
        return new_data
if __name__ == '__main__':
    get=getExcelData()
    data=get.assembData()
    print(data)