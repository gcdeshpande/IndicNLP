# Example 1 - Get Embedding Vectors
from inltk.inltk import setup
from inltk.inltk import tokenize
from inltk.inltk import get_embedding_vectors
'''
Note: You need to run setup('<code-of-language>') when you use a language for the FIRST TIME ONLY.
This will download all the necessary models required to do inference for that language.
'''
setup('hi')
example_sent = "बहुत समय से मिले नहीं"
# Tokenize the sentence
example_sent_tokens = tokenize(example_sent,'hi')
# Get the embedding vector for each token
example_sent_vectors = get_embedding_vectors(example_sent, 'hi')
print("Tokens:", example_sent_tokens)
print("Number of vectors:", len(example_sent_vectors))
print("Shape of each vector:", len(example_sent_vectors[0]))
