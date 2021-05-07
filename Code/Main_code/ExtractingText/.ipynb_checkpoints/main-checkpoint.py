import PyPDF2
a = PyPDF2.PdfFileReader('QuarterlyReport.pdf')

str = ""

for i in range(1, 44):
    str += a.getPage(i).extractText()


with open("ExtractedText.txt", "w", encoding='utf-8') as f:
    f.write(str)