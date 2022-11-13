import re
directoryPathSource_bahnstadt = './bahnstadt_PyPDF2.txt'

output = open('./Problem1-3.3(ii).txt', 'a')

# Outputdatei füllen und Format normalisieren
def fill_Output(match):
    print(match)
    output.write(match + '\n')

print("#-------------------------")
print("BAHNSTADT-URL")
print("#-------------------------")
url_in_bahnstadt = open(directoryPathSource_bahnstadt, 'r')
lines_bahnstadt = url_in_bahnstadt.readlines()

for line in lines_bahnstadt:
    url_match_de = re.findall(r"www.[a-zA-Z0-9_.-/]+.[a-zA-Z0-9_.-/]+[a-zA-Z0-9_.-/]\.[de|com]*", line, re.IGNORECASE)
    for url in url_match_de:
        fill_Output(url)

print("#-------------------------")
print("BAHNSTADT-E-Mail")
print("#-------------------------")

for line in lines_bahnstadt:
    url_match = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.].+?(?=\s|,|[\)]|[A-Z])", line)
    for url in url_match:
        fill_Output(url)

