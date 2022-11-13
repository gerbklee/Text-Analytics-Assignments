import re

directoryPathDestination_wegweiser = './wegweiser_senioren.txt'

output = open('./Problem1-3.3(ii).txt', 'a')


def fill_Output(match):
    print(match)
    output.write(match + '\n')


url_in_wegweiser = open(directoryPathDestination_wegweiser, 'r')
lines_wegweiser = url_in_wegweiser.readlines()

# TODO Trefferquote 171 von 174 - --> 3 E-Mails, die mit Umbruch getrennt werden, werden nicht mit einbezogen!!!
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

for url in url_match:
    cleaned = re.sub(r'\.$', '', url)
    fill_Output(cleaned)
