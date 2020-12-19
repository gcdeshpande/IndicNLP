from inltk.inltk import get_sentence_similarity

# similarity of encodings is calculated by using cmp function whose default is cosine similarity
get_sentence_similarity('भारत एक अद्भुत देश है।', 'ऋषि-मुनियों और अवतारों की भूमि 'भारत' एक रहस्यमय देश है।', 'hi')
