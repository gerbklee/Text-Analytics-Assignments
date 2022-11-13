import re
directoryPathDestination_bundeswehr = './bundeswehr_daten.txt'

url_in_bundeswehr = open(directoryPathDestination_bundeswehr, 'r')
lines_bundeswehr = url_in_bundeswehr.readlines()

output = open('./Problem1-3.3(ii).txt', 'a')


def fill_Output(match):
    print(match)
    output.write(match + '\n')

#TODO Bei Umbrüchen kommt für Email und URL ein "-", der wird mit eingelesen (müsste aber für valide Mail/URL weg sein)

print("#-------------------------")
print("BUNDESWEHR-E-Mail")
print("#-------------------------")

for line in lines_bundeswehr:
    url_match = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.].+?(?=h|[\s])", line)
    for url in url_match:
        fill_Output(url)

print("#-------------------------")
print("BUNDESWEHR-URL")
print("#-------------------------")

for line in lines_bundeswehr:
    url_match = re.findall(r"[http|https]+://www.[a-zA-Z0-9_.-/]+.[a-z]+.[a-z].+?(?=\s)", line)
    for url in url_match:
        if(re.search("\.\.", url)):
            continue
        cleaned = re.sub(r'^t', '', url)
        fill_Output(cleaned)