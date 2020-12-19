from indicnlp.tokenize import indic_tokenize  
from collections import Counter

indic_string='सुनो, कुछ आवाज़ आ रही है। फोन?'
x=[]

stopwords={"है","।","?"}
print('Input String: {}'.format(indic_string))
print('Tokens: ')
for t in indic_tokenize.trivial_tokenize(indic_string): 
  x.append(t)
  print(t)

print(x)

my_doc = [ele for ele in x if ele not in stopwords] 
print("\nToken List after Preprocessing")
print(my_doc)
print("\n")

print('After PreProcessing n_Tokens: ', len(my_doc))
print("\n")

print("Word frequency of Grams");
gram=Counter(my_doc)
print(gram)
gram=sorted(gram, key=lambda i: gram[i], reverse=True)[:10]
print("\nTop 10 grams");
print(gram)
print("\n")


print("Word frequency of Bigrams");
bigram=Counter(zip(my_doc[::],my_doc[1::]))
print(bigram)
bigram=sorted(bigram, key=lambda i: bigram[i], reverse=True)[:10]
print("\nTop 10 Bigrams");
print(bigram)
print("\n")
