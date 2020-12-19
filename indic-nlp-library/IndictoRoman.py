from indicnlp.transliterate.unicode_transliterate import ItransTransliterator

input_text='आज मौसम अच्छा है। इसलिए हम आज खेल सकते हैं!'

# Transliterate Hindi to Roman
print(ItransTransliterator.to_itrans(input_text, 'kn'))
