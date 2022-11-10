def removedDuplicates(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
    unique = set(lines)

    with open(fileName + ".Unique", "w") as f:
        for word in unique:
            f.write(word)

removedDuplicates("Problem1-3.3(i).txt")
removedDuplicates("Problem1-3.3(ii).txt")
removedDuplicates("Problem1-3.3(iii).txt")

print("Fertig.")