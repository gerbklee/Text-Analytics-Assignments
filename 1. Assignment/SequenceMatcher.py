import difflib

plumper_in = open('bahnstadt_plumber.txt', 'rb')

with plumper_in as text_file_plumper:
    plumper_txt = text_file_plumper.readlines()

pypdf_in = open('bahnstadt_pyPdf.txt', 'rb')

with pypdf_in as text_file_pypdf:
    pypdf_txt = text_file_pypdf.readlines()

temp = difflib.SequenceMatcher(None, plumper_txt, pypdf_txt)

print(temp.get_matching_blocks())
print('Quick ratio: ', temp.quick_ratio())
print('Similarity Score: ', temp.ratio())

text_file_pypdf.close()
text_file_plumper.close()