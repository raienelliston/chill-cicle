import xlsxSheet as xlsx

class sheets():
    def __init__(self, type):
        if type == xlsx:
            self.sheet = xlsx.xlsx()

    def appendList(self, list):
        self.sheet.appendList(list)

    def export(self, location = "export.xlsx"):
        self.sheet.export(location)

if __name__ == "__main__":
    sheets = sheets(xlsx)
    sheets.appendList([[1,2,3],[4,5,6]])
    sheets.export("test.xlsx")