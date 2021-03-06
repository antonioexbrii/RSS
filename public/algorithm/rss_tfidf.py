import json
import os
import math
import re
import glob


def looper():
    if os.path.exists("deposit.json"):
        nn = open('deposit.json', 'w', encoding='utf-8')
        nn.write('')
    if os.path.exists("algorithm.json"):
        nn = open('algorithm.json', 'w', encoding='utf-8')
        nn.write('')
    if os.path.exists("rssnews.json"):
        nn = open('rssnews.json', 'w', encoding='utf-8')
        nn.write('')
    for filename in glob.glob('../data/*.json'):
        nf = open(filename,
                  "r", encoding="utf-8")
        dumpNews(nf)


def dumpNews(nf):
    gn = open('deposit.json', "r", encoding="utf-8")
    wordCount = {}
    if not os.stat('deposit.json').st_size == 0:
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
    rn = open('rssnews.json', 'r', encoding='utf-8')
    if not os.stat('rssnews.json').st_size == 0:
        rssnews = json.load(rn)
        rsselem["entries"] = rssnews["entries"]
        rn.close()
    for n in newEntries["entries"]:

        rsselem["entries"].append(n)
    rssSize = len(rsselem["entries"])
    rsselem["count"] = rssSize
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
    depSize = newEntries["count"]
    element = {
        "collection": []
    }
    for k in newEntries["entries"]:
        insert = {
            "sentence": k["sentence"],
            "title": k["title"],
            "words": [],
            "sentence_tfidf": 0
        }
        words = k["sentence"].split()
        unique = []
        count = 0
        total = 0
        for word in words:
            if not word in unique:
                tf = calculateTF(words, word)
                idf = calculateIDF(word, deposit, depSize)
                total += tf * idf
                count += 1
                welem = {
                    "word": word,
                    "tf": tf,
                    "idf": idf
                }
                insert["words"].append(welem)
                unique.append(word)
        insert["sentence_tfidf"] = total / count
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


looper()
tf_idf()
