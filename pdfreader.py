import PyPDF2
pdfobj = open('Automate the Boring Stuff with Python.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfobj)
print(pdfReader.numPages)

pagesobj = pdfReader.getPage(10)
pagesobj.extractText()
