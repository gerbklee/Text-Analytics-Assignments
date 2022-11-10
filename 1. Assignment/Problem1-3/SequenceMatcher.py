import difflib

#####
markierterText_acrobat = open('bahnstadtAdobeAcrobatReaderAllesMarkiert.txt', 'rb')
with markierterText_acrobat as markierterText_acrobat:
    markierterText_txt_acrobat = markierterText_acrobat.readlines()

#####
plumper_in = open('bahnstadt_plumber.txt', 'rb')
with plumper_in as text_file_plumper:
    plumper_txt = text_file_plumper.readlines()

#####
pypdf_in = open('bahnstadt_PyPDF2.txt', 'rb')
with pypdf_in as text_file_pypdf:
    pypdf_txt = text_file_pypdf.readlines()

#####
temp = difflib.SequenceMatcher(None, plumper_txt, pypdf_txt)

print(temp.get_matching_blocks())
print('Quick ratio: ', temp.quick_ratio())
print('Similarity Score: ', temp.ratio())

text_file_pypdf.close()
text_file_plumper.close()
markierterText_acrobat.close()

# Vergleich

print('Vergleich man. kopiert mit Plumber  : ', difflib.SequenceMatcher(None, plumper_txt, markierterText_txt_acrobat).ratio())

print('Vergleich man. kopiert mit PyPDF2  : ', difflib.SequenceMatcher(None, pypdf_txt, markierterText_txt_acrobat).ratio())