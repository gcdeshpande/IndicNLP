from inltk.inltk import setup
from inltk.inltk import predict_next_words

# download models for Hindi
setup('bn')
# predict the next words of the sentence "The weather is nice today"
predict_next_words("भारत एक अद्भुत देश है", 10, "hi", 0.7)
