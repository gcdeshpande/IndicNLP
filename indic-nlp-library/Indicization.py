from indicnlp.transliterate.unicode_transliterate import ItransTransliterator

input_text='pAlakkAda'
# input_text='pitL^In'
lang='ml'
x=ItransTransliterator.from_itrans(input_text,lang)
print(x)
for y in x:
    print('{:x}'.format(ord(y)))
