import json
import os
import math
import re


def dumpNews():
    nf = open('entry.json', "r", encoding="utf-8")
    wordCount = {}
    if not os.stat('deposit.json').st_size == 0:
        gn = open('deposit.json', "r", encoding="utf-8")
        deposit = json.load(gn)
        for d in deposit['entries']:
            wordCount[d["word"]] = d["count"]
            gn.close()
    newEntries = json.load(nf)
    for k in newEntries["entries"]:
        tmp = re.sub(r'\.', '', k["sentence"])
        words = tmp.split()
        distinct = {}
        for wrd in words:
            word = wrd.lower()
            if not word in distinct:
                distinct[word] = 1
        for w in distinct:
            if w in wordCount:
                wordCount[w] = wordCount[w]+1
            else:
                wordCount[w] = 1
    element = {
        "entries": []
    }
    for w in wordCount:
        element["entries"].append({"word": w, "count": wordCount[w]})
    str2 = json.dumps(element, ensure_ascii=False).encode('utf-8')
    gn = open('deposit.json', "w", encoding="utf-8")
    gn.write(str2.decode('utf-8'))
    rsselem = {
        "entries": []
    }
    if not os.stat('rssnews.json').st_size == 0:
        rn = open('rssnews.json', 'r', encoding='utf-8')
        rssnews = json.load(rn)
        rsselem["entries"] = rssnews["entries"]
        rn.close()
    for n in newEntries["entries"]:
        rsselem["entries"].append(n)
    rn = open('rssnews.json', 'w', encoding='utf-8')
    dmp1 = json.dumps(rsselem, ensure_ascii=False).encode('utf-8')
    rn.write(dmp1.decode('utf-8'))
    rn.close()
    nf.close()
    gn.close()


def tf_idf():
    nf = open('rssnews.json', "r", encoding="utf-8")
    gn = open('deposit.json', "r", encoding="utf-8")
    newEntries = json.load(nf)
    deposit = json.load(gn)
    depSize = len(deposit["entries"])
    element = {
        "collection": []
    }
    for k in newEntries["entries"]:
        insert = {
            "sentence": k["sentence"],
            "words": []
        }
        words = k["sentence"].split()
        for word in words:
            tf = calculateTF(words, word)
            idf = calculateIDF(word, deposit, depSize)
            welem = {
                "word": word,
                "tf": tf,
                "idf": idf
            }
            insert["words"].append(welem)
        element["collection"].append(insert)
    nn = open('algorithm.json', 'w', encoding='utf-8')
    str2 = json.dumps(element, ensure_ascii=False).encode('utf-8')
    nn.write(str2.decode('utf-8'))
    nf.close()
    gn.close()


def calculateTF(sentence, word):
    totalWords = 0
    ocurrences = 0
    for w in sentence:
        totalWords = totalWords+1
        if w == word:
            ocurrences = ocurrences+1

    return ocurrences/totalWords


def calculateIDF(word, deposit, total):
    ocurrences = 1
    for w in deposit["entries"]:
        if word == w["word"]:
            ocurrences = w["count"]
    return math.log10(total/ocurrences)


dumpNews()
tf_idf()
