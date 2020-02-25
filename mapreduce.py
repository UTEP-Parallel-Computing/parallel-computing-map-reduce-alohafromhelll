import re
import pymp
import timeit


#docs = "hate love death night death"

#read files
with open('shakespeare1.txt', 'r') as f:
    doc1 = f.read()

with open('shakespeare2.txt', 'r') as f:
    doc2 = f.read()

with open('shakespeare3.txt', 'r') as f:
    doc3 = f.read()

with open('shakespeare4.txt', 'r') as f:
    doc4 = f.read()

with open('shakespeare5.txt', 'r') as f:
    doc5 = f.read()

with open('shakespeare6.txt', 'r') as f:
    doc6 = f.read()

with open('shakespeare7.txt', 'r') as f:
    doc7 = f.read()

with open('shakespeare8.txt', 'r') as f:
    doc8 = f.read()


#combine files into one big string and lowercase
docs = doc1 + doc2 + doc3 + doc4 + doc5 + doc6 + doc7 + doc8
docs = docs.lower()

wordlist = [ "hate", "love", "death", "night", "sleep", "time",
            "henry", "hamlet", "you", "my", "blood", "poison", "macbeth",
            "king", "heart", "honest"
            ]


def count_words(wordlist, document):
    result = pymp.shared.dict()

    with pymp.Parallel(16) as p:
        for word in wordlist:
            result.update({word : 0})

        #create lock
        sumLock = p.lock

        for words in p.iterate(wordlist):
            pattern = re.compile(r''+words+'')
            if re.findall(pattern,document):
                length = len(re.findall(pattern,document))
                #lock
                sumLock.acquire()
                result[words] += length
                #release
                sumLock.release()
    return result



#start timer
start = timeit.default_timer()

print (count_words(wordlist, docs))
#stop timer
stop = timeit.default_timer()
#print time
print('Time: ', stop - start)
