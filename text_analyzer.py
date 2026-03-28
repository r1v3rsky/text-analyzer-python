import locale
from sys import argv
locale.setlocale(locale.LC_ALL, "en_US")

f_in = open(argv[1], "r")
readtxt = f_in.read()
f_out = open(argv[2], "w")
def main ():
    x= "Statistics about"
    f_out.write("{} {:7}:".format(x,argv[1]))
    calculatePerWtSt()
    calculateChar()
    calculateCharWithoutP()
    shortestLongestandFrequencies()
    f_in.close()
    f_out.close()

def calculateWords(): #count words
    numberofwords = 0
    listoftxtwords = readtxt.split()
    for i in listoftxtwords:
        numberofwords += 1
    a = "#Words"
    f_out.write("\n{:24}: {}".format(a,numberofwords) )
    return numberofwords

def calculateSentences (): #count sentences
    numberofsentences = 0
    finishsentences = ["?", "!", "..."]
    listwords = readtxt
    for i in finishsentences:
        listwords = listwords.replace(i,".")

    listoftxtwords = listwords.split(".")
    for i in listoftxtwords:
        numberofsentences += 1
    a = "#Sentences"
    f_out.write("\n{:24}: {}".format(a, numberofsentences -1))
    return numberofsentences-1 #When it divides sentences based on dot, there is one empty element in list. So we need to subtract 1.

def calculatePerWtSt(): #count words per sentence
    numberwords = calculateWords()
    numberofsentences = calculateSentences()
    a="#Words/#Sentences"
    f_out.write("\n{:24}: {:.2f}".format(a, numberwords/numberofsentences))

def calculateChar(): #count all characters
    listoftxtwords = list(readtxt)
    a="#Characters"
    f_out.write("\n{:24}: {}".format(a, len(listoftxtwords)))

def calculateCharWithoutP(): #count just words characters
    punctuations = [ ".", "\n","\t", "[", "]", ",", "!", "' ", "/", "?", "(", ")", ";", "- ", "{", "}", ":", "@", "#", "$", "%", "^", "&", "*", "_", "~", "^", " "]
    withoutpunc = readtxt
    for i in punctuations:
        withoutpunc = withoutpunc.replace(i, "")
    listoftxtwords = list(withoutpunc)
    a = "#Characters (Just Words)"
    f_out.write("\n{:24}: {}".format(a, len(listoftxtwords)))

def shortestLongestandFrequencies(): #find shortest and longest words and find frequencies of words
    listofwords = readtxt.strip()
    puncs = ["[", "]","{", "}","[ ", "] ","{ ", "} ", ". ",". ",".\n",".","\n" ,"/ ", "? ","?" "; ",";", ": ", "' ",",", ", ", "< ", "> ","^ " , "<", ">", " #", "! ", "!","(", ")","( ", ") ", "- ", "[ ", "] ","* "]
    #There are punctuations with spaces and it prevents to remove punctuations included in words. (Especially ' and -)
    for i in puncs:
        listofwords = listofwords.replace(i," ")

    wordslist = listofwords.split(" ")
    wordslist = [word.lower() for word in wordslist if word]
    shortest = wordslist[0].strip()
    longest = wordslist[0].strip()
    for liste in wordslist:
        if len(liste) < len(shortest):
            shortest = liste
        if len(liste) > len(longest):
            longest = liste
        newlistshort = set()
        newlistshort.add(shortest)
        newlistlong = set()
        newlistlong.add(longest.lower())
        for a in wordslist:
            if len(a) == len(shortest):
                newlistshort.add(a)
            if len(a) == len(longest):
                newlistlong.add(a)

    dictionary = {}
    for everywords in wordslist:
        everywordslower = everywords.lower()
        counter = 0
        for otherword in wordslist:
            otherwordlower = otherword.lower()
            if everywordslower == otherwordlower:
                counter +=1
        ratio = counter / len(wordslist)
        dictionary[everywordslower] = ratio
    sorted_items = sorted(dictionary.items(), key=lambda x: (-x[1],x[0]))
    n="The Shortest Word"
    if len(newlistshort)==1:
        for x in newlistshort:
            f_out.write("\n{:24}: {:24} ({:.4f})".format(n, x, dictionary[x.lower()]))
    else:
        s="The Shortest Words"
        f_out.write("\n{:24}:".format(s))
        for y in sorted(newlistshort):
            f_out.write("\n{:24} ({:.4f})".format(y,dictionary[y.lower()]))

    m = "The Longest Word"
    if len(newlistlong) == 1:
        for x in newlistlong:
            f_out.write("\n{:24}: {:24} ({:.4f})".format(m, x, dictionary[x.lower()]))
    else:
        s = "The Longest Words"
        f_out.write("\n{:24}:".format(s))
        for y in sorted(newlistlong):
            f_out.write("\n{:24} ({:.4f})".format(y, dictionary[y.lower()]))
    a = "Words and Frequencies"
    f_out.write("\n{:24}:".format(a))
    for key, value in sorted_items:
        f_out.write("\n{:24}: {:.4f}".format(key, value))

if __name__ == "__main__":
    main()