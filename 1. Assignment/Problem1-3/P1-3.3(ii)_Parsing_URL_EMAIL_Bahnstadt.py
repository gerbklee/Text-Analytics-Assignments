import re
directoryPathDestination_bahnstadt = './bahnstadt.txt'

output = open('./Problem1-3.3(ii).txt', 'a')


def fill_Output(match):
    print(match)
    output.write(match + '\n')

print("#-------------------------")
print("BAHNSTADT-URL")
print("#-------------------------")
url_in_bahnstadt = open(directoryPathDestination_bahnstadt, 'r')
lines_bahnstadt = url_in_bahnstadt.readlines()

#TODO URLs mit "/" wird der Teil mit "/" abgeschnitten??????
for line in lines_bahnstadt:
    url_match_de = re.findall(r"www.[a-zA-Z0-9_.-/]+.[a-zA-Z0-9_.-/]+[a-zA-Z0-9_.-/]\.[de|com]*", line, re.IGNORECASE)
    for url in url_match_de:
        fill_Output(url)

#TODO 97 von 100 Trefferquote --> 3 E-Mails, die mit Umbruch getrennt werden, werden nicht mit einbezogen!!!
print("#-------------------------")
print("BAHNSTADT-E-Mail")
print("#-------------------------")

for line in lines_bahnstadt:
    url_match = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.].+?(?=\s|,|[\)]|[A-Z])", line)
    for url in url_match:
        fill_Output(url)

