file = open("bahnstadt_plumber.txt", "rt")
data = file.read()
words = data.split()
print('Number of words in text file plumber :', len(words))
file.close()

file = open("bahnstadt_pyPdf.txt", "rt")
data = file.read()
words = data.split()
print('Number of words in text file pyPdf :', len(words))
file.close()