from inltk.inltk import get_embedding_vectors

# get embedding for input words
vectors = get_embedding_vectors("भारत एक अद्भुत देश है", "hi")

print(vectors)
# print shape of the first word
print("shape:", vectors[0].shape)
