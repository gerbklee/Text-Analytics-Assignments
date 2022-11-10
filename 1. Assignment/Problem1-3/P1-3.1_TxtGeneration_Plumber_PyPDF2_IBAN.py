import PyPDF2
import time

directoryPathSource = './liste1.pdf'
directoryPathDestination = './liste1_PyPDF2.txt'

#-----------------
#liste1.txt mit PyPDF2
#-----------------

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
#liste1.txt mit Plumber
#-----------------

import pdfplumber

directoryPathSource = './liste1.pdf'
directoryPathDestination = './liste1_Plumber.txt'

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