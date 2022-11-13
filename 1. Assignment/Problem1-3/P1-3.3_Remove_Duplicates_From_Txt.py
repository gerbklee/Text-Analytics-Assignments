# Duplikate in Outputdateien beseitigen
def removeDuplicates(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
    unique = set(lines)

    with open(fileName + ".Unique", "w") as f:
        for word in unique:
            f.write(word)

removeDuplicates("Problem1-3.3(i).txt")
removeDuplicates("Problem1-3.3(ii).txt")
removeDuplicates("Problem1-3.3(iii).txt")

print("Fertig.")