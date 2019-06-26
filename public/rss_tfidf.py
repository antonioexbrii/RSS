import json
import os
# meter um id no scrapy


def dumpNews():
    nf = open('rssnews.json', "r", encoding="utf-8")
    wordCount = {}
    # ver se nao esta vazio
    if not os.stat('deposit.json').st_size == 0:
        gn = open('deposit.json', "r", encoding="utf-8")
        deposit = json.load(gn)
        for d in deposit['entries']:
            wordCount[d["word"]] = d["count"]
            gn.close()
    newEntries = json.load(nf)
    for k in newEntries["entries"]:
        words = k["sentence"].split()
        for wrd in words:
            word = wrd.lower()
            if word in wordCount:
                wordCount[word] = wordCount[word]+1
            else:
                wordCount[word] = 1
    element = {
        "entries": []
    }
    for w in wordCount:
        element["entries"].append({"word": w, "count": wordCount[w]})
    str2 = json.dumps(element, ensure_ascii=False).encode('utf-8')
    gn = open('deposit.json', "w", encoding="utf-8")
    gn.write(str2.decode('utf-8'))


dumpNews()
