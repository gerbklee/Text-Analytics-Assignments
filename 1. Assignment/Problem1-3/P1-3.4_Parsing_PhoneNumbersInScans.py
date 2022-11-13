import re

#Vorgehensweise wie für Telefonnummer-Parsing bei Bahnstadt

directoryPathSource_doubleOcr = './double_ocr_PyPDF.txt'
directoryPathSource_singleOcr = './single_ocr_PyPDF.txt'

output = open('./Problem1-3.4.txt', 'w')

# Outputdatei füllen und Format normalisieren
def fill_Output(match):
    cleaned = re.sub(r' ', '', match)
    cleaned = re.sub(r'-', '', cleaned)
    cleaned = re.sub(r'/', '', cleaned)
    cleaned = re.sub(r'\(', '', cleaned)
    cleaned = re.sub(r'\)', '', cleaned)
    print(cleaned)
    output.write(cleaned + '\n')

print("#-------------------------")
print("Double_ocr-Telefon")
print("#-------------------------")

url_in_doubleOcr = open(directoryPathSource_doubleOcr, 'r')
lines_doubleOcr = url_in_doubleOcr.readlines()

telefonNumbersGesamtDoubleOcr = []

for line in lines_doubleOcr:
    line = line.replace(" ", "")
    telefonNumbers = re.findall(r"(?:\(\+?\d+\)|\+?\d+)(?:\s*[\-\/]*\s*\d+)+", line)
    if (telefonNumbers):
        telefonNumbersGesamtDoubleOcr.extend(telefonNumbers)

# Spezielle Nummern
for nummer in telefonNumbersGesamtDoubleOcr:
    if (len(nummer) > 5 or nummer == '112' or nummer == '110'):
        fill_Output(nummer)

url_in_doubleOcr.close()

print("#-------------------------")
print("Single_ocr-Telefon")
print("#-------------------------")

url_in_singleOcr = open(directoryPathSource_singleOcr, 'r')
lines_singleOcr = url_in_singleOcr.readlines()

telefonNumbersGesamtSingleOcr = []

for line in lines_singleOcr:
    line = line.replace(" ", "")
    telefonNumbers = re.findall(r"(?:\(\+?\d+\)|\+?\d+)(?:\s*[\-\/]*\s*\d+)+", line)
    if (telefonNumbers):
        telefonNumbersGesamtSingleOcr.extend(telefonNumbers)

# Spezielle Nummern
for nummer in telefonNumbersGesamtSingleOcr:
    if (len(nummer) > 5 or nummer == '112' or nummer == '110'):
        fill_Output(nummer)

url_in_singleOcr.close()