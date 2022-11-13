# Parsing for IBAN
import re

directoryPathSource = './liste1_PyPDF2.txt'
output = open('./Problem1-3.3(iii).txt','w')

# Outputdatei füllen und Format normalisieren
def fill_Output(match):
    print(match)
    output.write(match + '\n')

iban_in = open(directoryPathSource, 'r')
lines = iban_in.readlines()

for line in lines:
    laendercodematch = re.search(r"[a-zA-Z]{2}[0-9]{2}", line)
    if(laendercodematch):
        substring = (line[laendercodematch.start():])
        substringWithoutSpaces = substring.replace(" ", "")
        match = re.search(r"[a-zA-Z]{2}[0-9]{2}[a-zA-Z0-9]{4}[0-9]{7}([a-zA-Z0-9]?){0,16}", substringWithoutSpaces)
        if(match):
            fill_Output(substringWithoutSpaces[match.start():match.end()])

iban_in.close()