import openpyxl

class xlsx:
    def __init__(self, file_path = None):
        if file_path:
                self.workbook = openpyxl.load_workbook(file_path)
        else:
            self.workbook = openpyxl.Workbook()
            self.worksheet = self.workbook.active

    def appendList(self, list):
        for row in list:
            self.worksheet.append(row)

    def export(self, location = "export.xlsx"):
        self.workbook.save(location)

if __name__ == "__main__":
    xlsx = xlsx()
    xlsx.appendList([[1,2,3],[4,5,6]])
    xlsx.export("test.xlsx")