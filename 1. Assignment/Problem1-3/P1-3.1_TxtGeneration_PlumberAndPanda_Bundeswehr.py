import pdfplumber
import pandas as pd

directoryPathSource = './bundeswehr.pdf'

file = open('bundeswehr_daten.txt', 'w')

#-----------------
#bundeswehr.txt mit Plumber and Panda
#-----------------

with pdfplumber.open(directoryPathSource) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        pdframe = pd.DataFrame(table[1::], columns=table[0])
        df1 = pd.DataFrame(pdframe, columns=['Telefon', 'Telefon(IV\nBB)', 'E-Mail und URL'])
        for column in ['Telefon', 'Telefon(IV\nBB)', 'E-Mail und URL']:
            df1[column] = df1[column].str.replace("\n", "")
        file.write(df1.to_string(index=False, header=False))

file.close()