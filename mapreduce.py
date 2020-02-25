import re
import pymp
import timeit

docs = []
doc1 = "the the the the time time time we love love love spent together spent"

#doc2 = "i've spent some time together"
#with open('shakespeare1.txt', 'r') as f:
    #doc1 = f.read()
    #docs.append(doc1)

#with open('shakespeare2.txt', 'r') as f:
    #doc1 = f.read()
    #docs.append(doc1)

# with open('shakespeare3.txt', 'r') as f:
#     doc3 = f.read()
#     docs.append(doc3)
#
# with open('shakespeare4.txt', 'r') as f:
#     doc4 = f.read()
#     docs.append(doc4)
#
# with open('shakespeare5.txt', 'r') as f:
#     doc5 = f.read()
#     docs.append(doc5)
#
# with open('shakespeare6.txt', 'r') as f:
#     doc6 = f.read()
#     docs.append(doc6)
#
# with open('shakespeare7.txt', 'r') as f:
#     doc7 = f.read()
#     docs.append(doc7)
#
# with open('shakespeare8.txt', 'r') as f:
#     doc8 = f.read()
#     docs.append(doc8)
wordlist = [ "hate", "love", "death", "night", "sleep", "time"]
result = pymp.shared.dict()

for word in wordlist:
    result.update({word : 0})



def count_words(wordlist, document, result):

    newlist = re.findall(r"\w+", document)

    with pymp.Parallel(8) as p:

        #print("hello")
        #sumLock = p.lock
        #print(newlist)

        for w in p.iterate(newlist):
            #print("hello")
            if w in result:
                #sumLock.acquire()
                #lock
                result[w] += 1
                #sumLock.release()
                #release lock
    return result



#print(wc)
#print(docs[0])







#start timer
start = timeit.default_timer()

#for doc in docs:
#wordcount = count_words(wordlist, doc1)
print (count_words(wordlist, doc1, result))
#stop timer
stop = timeit.default_timer()
#print time
print('Time: ', stop - start)
