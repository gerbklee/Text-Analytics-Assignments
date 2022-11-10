import re

directoryPathDestination_wegweiser = './wegweiser_senioren.txt'
directoryPathDestination_bundeswehr = './bundeswehr_daten.txt'
directoryPathDestination_bahnstadt = './bahnstadt.txt'

output = open('./Problem1-3.3(i).txt','w')

def fill_Output(match):
    cleaned = re.sub(r' ', '', match)
    cleaned = re.sub(r'-', '', cleaned)
    cleaned = re.sub(r'/', '', cleaned)
    cleaned = re.sub(r'\(', '', cleaned)
    cleaned = re.sub(r'\)', '', cleaned)
    print(cleaned)
    output.write(cleaned + '\n')

print("#-------------------------")
print("Bundeswehr-Telefon")
print("#-------------------------")

url_in_Bundeswehr = open(directoryPathDestination_bundeswehr, 'r')
lines_Bundeswehr = url_in_Bundeswehr.readlines()

telefonNumbersGesamtBundeswehr = []

for line in lines_Bundeswehr:
    #alle +49 Nummern
    telephoneNumbers = re.findall(r"\+[0-9|\s]{2}[\s|0-9|\-|\(|\)]{1,20}", line)
    #alle 0800er Nummern
    telephoneNumbers2 = re.findall(r"0800+[\s|\-|0-9]{1,15}", line)
    telefonNumbersGesamtBundeswehr.extend(telephoneNumbers)
    telefonNumbersGesamtBundeswehr.extend(telephoneNumbers2)

for nummer in telefonNumbersGesamtBundeswehr:
    cleaned = re.sub(r'\($', '', nummer)
    fill_Output(cleaned)

url_in_Bundeswehr.close()

print("#-------------------------")
print("Senioren-Telefon")
print("#-------------------------")

url_in_wegweiser = open(directoryPathDestination_wegweiser, 'r')
lines_wegweiser = url_in_wegweiser.readlines()

telefonNumbersGesamtWegweiser = []

for line in lines_wegweiser:
    new_text = re.sub(r"[^a-zA-Z0-9 ()]", "", line)
    telephoneNumbers = re.findall(r"\([0-9 ]+\)[0-9- ]+", new_text)
    telefonNumbersGesamtWegweiser.extend(telephoneNumbers)


for nummer in telefonNumbersGesamtWegweiser:
    fill_Output(nummer)

url_in_wegweiser.close()

print("#-------------------------")
print("Bahnstadt-Telefon")
print("#-------------------------")

url_in_bahnstadt = open('./bahnstadt.txt', 'r')
lines_bahnstadt = url_in_bahnstadt.readlines()

telefonNumbersGesamtBahnstadt = []

for line in lines_bahnstadt:
    line = line.replace(" ", "")
    telefonNumbers = re.findall(r"(?:\(\+?\d+\)|\+?\d+)(?:\s*[\-\/]*\s*\d+)+", line)
    if(telefonNumbers):
        # Alles in ein Array rein
        telefonNumbersGesamtBahnstadt.extend(telefonNumbers)

for nummer in telefonNumbersGesamtBahnstadt:
    if(len(nummer) > 5  or nummer == '112' or nummer == '110'):
        fill_Output(nummer)

url_in_bahnstadt.close()