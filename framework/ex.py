import xlrd
from framework.logger import *

logger=Logger(logger="Ex").getlog()
class Ex(object):
    @classmethod
    def read_ex(self,exPath,sheetName='Sheet1'):

        work=xlrd.open_workbook(exPath)
        sheet=work.sheet_by_name(sheetName)

        keys=sheet.row_values(0)
        rowNum=sheet.nrows
        cloNum=sheet.ncols

        if rowNum<=1:
            logger.error('excel表中数据总行数小于1')
        else:
            r=[]
            for i in range(1,rowNum):
                sheet_data={ }
                valuse=sheet.row_values(i)
                for j in range(0,cloNum):
                    sheet_data[keys[j]]=valuse[j]
                r.append(sheet_data)
            return r

if __name__=="__main__":
    wo_path = os.path.dirname(os.path.abspath('.'))+'/excel/工作簿.xlsx'
    print(Ex.read_ex(wo_path))