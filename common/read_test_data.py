import openpyxl


class ReadExcel(object):
    """读取excel"""

    @staticmethod
    def _open_excel(data_path):
        """打开Excel"""
        return openpyxl.load_workbook(data_path)

    def get_sheet(self, data_path, sheet_name):
        """定位到sheet表"""
        return self._open_excel(data_path=data_path)[sheet_name]

    def read_sheet(self, data_path, sheet_name):
        """读取数据"""
        work_sheet = self.get_sheet(data_path, sheet_name)
        # 读取首行数据作为key
        first_row = []
        rows = list(work_sheet.rows)
        for cell in rows[0]:
            first_row.append(cell.value)
        # 定义一个空列表来装读取出来的数据
        excel_data = []
        # 外循环：从第二行开始遍历直到最后一行
        for i in rows[1:]:
            detail = {}
            # 内循环：rows得到的是一个key：value形式的数据，遍历，获得下标和每一列的value，以key:value的形式添加到detail中
            for idx, cell in enumerate(i):
                detail[first_row[idx]]= cell.value
                # detail.update({first_row[idx]:cell.value})
            excel_data.append(detail)

        return excel_data

if __name__ == '__main__':
    test = ReadExcel()
    ret = test.read_sheet("/Users/apple/works/practice/api_test/data/data.xlsx", "news")
    print(ret)
