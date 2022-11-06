import time
import PyPDF2

directoryPathSource = './bahnstadt.pdf'
directoryPathDestination = './bahnstadt_pyPdf.txt'

file = open(directoryPathDestination, 'w')

begin = time.time()

with open(directoryPathSource, mode='rb') as pdf:
    pdfReader = PyPDF2.PdfFileReader(pdf)
    for page in pdfReader.pages:
        text = page.extractText()
        file.write(text)

end = time.time()

print("Laufzeit: ", end-begin)

file.close()
