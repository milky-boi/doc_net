# -*- coding: utf-8 -*-
"""
Dokumente je potrebno prilagoditi tako da se pojmovi prvo lematiziraju,
 a potom izbace ključne riječi. 

Nakon toga se iz dokumenata izvlači 
skup od n najvrekventnijih (ključnih riječi)
"""
import operator
import time
import re 
import string
#import matplotlib.pyplot as plt

from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer

now = time.strftime("%d.%m.%Y %H-%M")
start_time = time.time()

wordnet_lemmatizer = WordNetLemmatizer()

for y in range(30):
    a = open("clanci\sample %s.txt" % y, "r")
    a = a.read()
    
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    a = re.findall(r'\b[a-z]{2,25}\b', a)
    a = str(a)
    a = regex.sub('', a)
    
    
    example_sent = a
      
    stop_words = set(stopwords.words('english')) 
      
    word_tokens = a.split(" ")
      
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
      
    s = [] 
      
    for w in word_tokens: 
        if w not in stop_words: 
            s.append(w) 
           
          
    #s = s.split(" ")
    
    lemm = []
    for i in range (len(s)):
        word = wordnet_lemmatizer.lemmatize(s[i])
        lemm.append(word)
    
    ###################FREQ###############################
    frequency = {}
    
    for word in lemm:
        count = frequency.get(word,0)
        frequency[word] = count + 1
    
    duljina = (len (frequency))
    
    print("--- %s seconds ---\n" % (time.time() - start_time))
    
    frequency = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)  
    
    print (frequency[0])
    
    file = open("freq/freq_s %s.txt" % y, "w")
    
    for i in range (len(frequency)):
        word = str(frequency[i])
        file.write(word)

        file.write("\n")
    file.close()
    
###########uzimanje prvih 50 rijeci##########################
    nodes = open("freq/freq_s %s.txt" % y, "r")
    nodes = nodes.read()
    
    all_nodes = re.findall(r'\b[a-z]{2,15}\b', nodes)
    
    all_nodes_s = open("nodes/all_nodes_s %s.txt" % y, "w")
    
    for i in range (0, 50):
        word = str(all_nodes[i])
        all_nodes_s.write(word)
        all_nodes_s.write("\n")
    
    all_nodes_s.close()

"""     
    ###################GRAF###############################
    S = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
    xx = duljina
    
    plt.plot(*zip(*S))
    plt.xticks([xx])
    plt.title('Raspodjela frekvencija po rijecima u tekstu')
    plt.ylabel("freq")
    plt.xlabel("broj rijeci: " + str(duljina))
    plt.savefig('plot%s.png' % i, dpi=200)
    
"""   

###################################################


