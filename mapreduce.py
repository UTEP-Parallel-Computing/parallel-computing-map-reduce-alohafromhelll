import re
import pymp

docs = []
#doc1 = "the the the the time time time we love love love spent together spent"

#doc2 = "i've spent some time together"
with open('shakespeare1.txt', 'r') as f:
    doc1 = f.read()
    docs.append(doc1)

with open('shakespeare2.txt', 'r') as f:
    doc2 = f.read()
    docs.append(doc2)

with open('shakespeare3.txt', 'r') as f:
    doc3 = f.read()
    docs.append(doc3)

with open('shakespeare4.txt', 'r') as f:
    doc4 = f.read()
    docs.append(doc4)

wordlist = [ "hate", "love", "death", "night", "sleep", "time"]

#wordcount = dict((x,0) for x in wordlist)





def count_words(wordlist, document):
    newlist = re.findall(r"\w+", document)
    #newlist2 = pymp.shared.list()
    dumblist = ["love", "time", "spent"]
    #for x in newlist:
        #newlist2.append(x)
    #print(newlist2)
    wc = pymp.shared.dict()

    #add words to dictionary for results


    with pymp.Parallel(1) as p:
        sumLock = p.lock
        for word in wordlist:
            wc.update({word : 0})
        for w in p.iterate(newlist):
            #p.print(w)
            if w in wc:
                sumLock.acquire()
#lock
                wc[w] += 1
                sumLock.release()
                #release lock
    return wc



#print(doc1)
	#docs.append(doc1)






print(type(doc1))

for doc in docs:
    wordcount = count_words(wordlist, doc)

print(wordcount)







#findall finds all the matches and returns them as a list of strings
