import stanza

print("Downloading Hindi model...")
stanza.download('hi', verbose=False)

# Build a Hindi pipeline, with customized processor list and no logging, and force it to use CPU
print("Building a Hindi pipeline...")
hi_nlp = stanza.Pipeline('hi', processors='tokenize,lemma,pos,depparse', verbose=False, use_gpu=False)

hi_doc = hi_nlp("भारत एक अद्भुत देश है")
print(type(hi_doc))

for i, sent in enumerate(hi_doc.sentences):
    print("[Sentence {}]".format(i+1))
    for word in sent.words:
        print("{:12s}\t{:12s}\t{:6s}\t{:d}\t{:12s}".format(\
              word.text, word.lemma, word.pos, word.head, word.deprel))
    print("")
    
print("Mention text\tType\tStart-End")
for ent in hi_doc.ents:
    print("{}\t{}\t{}-{}".format(ent.text, ent.type, ent.start_char, ent.end_char))
    
word = hi_doc.sentences[0].words[0]
print(word)  
