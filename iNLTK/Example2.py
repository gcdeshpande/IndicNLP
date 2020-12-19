# Example 2 - Predict Next 'n' Words, Get Similar Sentences
from inltk.inltk import setup
from inltk.inltk import predict_next_words
from inltk.inltk import get_similar_sentences
'''
Note: You need to run setup('<code-of-language>') when you use a language for the FIRST TIME ONLY.
This will download all the necessary models required to do inference for that language.
'''
setup('ta')
example_sent = "உங்களைப் பார்த்து நிறைய நாட்கள் ஆகிவிட்டது"
# Predict next 'n' tokens
n = 5
pred_sent = predict_next_words(example_sent, n, 'ta')
# Get 'n' similar sentence
n = 2
simi_sent = get_similar_sentences(example_sent, n, 'ta')
print("Predicted Words:", pred_sent)
print("Similar Sentences:", simi_sent)
