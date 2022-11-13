import re

directoryPathSource_wegweiser = './wegweiser_senioren_PyPDF2.txt'

output = open('./Problem1-3.3(ii).txt', 'a')

# Outputdatei füllen und Format normalisieren
def fill_Output(match):
    print(match)
    output.write(match + '\n')


url_in_wegweiser = open(directoryPathSource_wegweiser, 'r')
lines_wegweiser = url_in_wegweiser.readlines()

print("#-------------------------")
print("Senioren-E-Mail")
print("#-------------------------")

for line in lines_wegweiser:
    url_match = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.].+?(?=\s)", line)
    for url in url_match:
        fill_Output(url)

print("#-------------------------")
print("SENIOREN-URL")
print("#-------------------------")

for line in lines_wegweiser:
    url_match = re.findall(r"www.[a-zA-Z0-9_.+-/].+?(?=[\s]|,|[\)])", line)

#manche URLs haben "." am Ende --> cleanen
for url in url_match:
    cleaned = re.sub(r'\.$', '', url)
    fill_Output(cleaned)
