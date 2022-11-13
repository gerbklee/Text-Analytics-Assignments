import re
directoryPathSource_bundeswehr = './bundeswehr_daten.txt'

url_in_bundeswehr = open(directoryPathSource_bundeswehr, 'r')
lines_bundeswehr = url_in_bundeswehr.readlines()

output = open('./Problem1-3.3(ii).txt', 'a')

# Outputdatei füllen und Format normalisieren
def fill_Output(match):
    print(match)
    output.write(match + '\n')


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
    #manche URLs haben ".." --> rausnehmen + "thttp" --> cleanen zu "http"
    for url in url_match:
        if(re.search("\.\.", url)):
            continue
        cleaned = re.sub(r'^t', '', url)
        fill_Output(cleaned)