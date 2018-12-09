from newspaper import Article 

urls = []
lenghts = []
with open('urls.txt') as f:
    content = f.readlines()
    

print (len(content))
print (content[0])
print (content[1])
for i in range(len(content)):
    #A new article from TOI 
    url = content[i]

    
    #For different language newspaper refer above table 
    toi_article = Article(url, language="en") # en for English 
      
    #To download the article 
    toi_article.download() 
      
    #To parse the article 
    toi_article.parse() 
      
    #To perform natural language processing ie..nlp 
    toi_article.nlp()

    title = str(toi_article.title)
    file = open("clanci\sample %s.txt" % i ,"w")

     
      
    #To extract text 
    file.write(toi_article.text.lower())
    print("clanak " + str(i) + " preuzet")

    words = toi_article.text.split(" ")
    lenght = len(words)
    lenghts.append(lenght)
    
    file.close()
    file = open("duljine.csv", "w")
    file.write(" name; words; \n")
    for i in range(len(lenghts)):
        file.write("s%s; " %(i+1))
        
        file.write(str(lenghts[i]))

        file.write(";\n")
    file.close()
    
