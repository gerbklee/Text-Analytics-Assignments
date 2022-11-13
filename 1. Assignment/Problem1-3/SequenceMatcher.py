import difflib

#####
markierterText_acrobat = open('bahnstadtAdobeAcrobatReaderAllesMarkiert.txt', 'rb')
with markierterText_acrobat as markierterText_acrobat:
    markierterText_txt_acrobat = markierterText_acrobat.readlines()

#####
plumber_in = open('bahnstadt_plumber.txt', 'rb')
with plumber_in as text_file_plumber:
    plumber_txt = text_file_plumber.readlines()

#####
pypdf_in = open('bahnstadt_PyPDF2.txt', 'rb')
with pypdf_in as text_file_pypdf:
    pypdf_txt = text_file_pypdf.readlines()

#####
temp = difflib.SequenceMatcher(None, plumber_txt, pypdf_txt)

print(temp.get_matching_blocks())
print('Quick ratio: ', temp.quick_ratio())
print('Similarity Score: ', temp.ratio())

text_file_pypdf.close()
text_file_plumber.close()
markierterText_acrobat.close()

# Vergleich

print('Vergleich manuell kopiert aus Acrobat Reader mit Plumber  : ', difflib.SequenceMatcher(None, plumber_txt, markierterText_txt_acrobat).ratio())

print('Vergleich manuell kopiert aus Acrobat Reader mit PyPDF2  : ', difflib.SequenceMatcher(None, pypdf_txt, markierterText_txt_acrobat).ratio())