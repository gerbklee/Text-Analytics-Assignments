import time
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

print("Laufzeit: ", end-begin)

file.close()
