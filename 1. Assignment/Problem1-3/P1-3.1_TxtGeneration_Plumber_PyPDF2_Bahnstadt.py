import time
import PyPDF2

#-----------------
#bahnstadt.txt mit PyPDF2
#-----------------

directoryPathSource = './bahnstadt.pdf'
directoryPathDestination = './bahnstadt_PyPDF2.txt'

file = open(directoryPathDestination, 'w')

begin = time.time()

with open(directoryPathSource, mode='rb') as pdf:
    pdfReader = PyPDF2.PdfFileReader(pdf)
    for page in pdfReader.pages:
        text = page.extractText()
        file.write(text)

end = time.time()

print("Laufzeit PyPDF2: ", end-begin)

file.close()
pdf.close()


#-----------------
#bahnstadt.txt mit Plumber
#-----------------

import pdfplumber

directoryPathSource = './bahnstadt.pdf'
directoryPathDestination = './bahnstadt_plumber.txt'

file = open(directoryPathDestination,"w")

begin = time.time()

with pdfplumber.open(directoryPathSource) as pdf:
    for pages in pdf.pages:
        text = pages.extract_text()
        file.write(text)

end = time.time()

print("Laufzeit Plumber: ", end-begin)

file.close()
pdf.close()