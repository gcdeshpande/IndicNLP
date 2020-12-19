from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator

# Input text "Today the weather is good. Sun is bright and there are no signs of rain. Hence we can play today."
input_text='आज मौसम अच्छा है। सूरज उज्ज्वल है और बारिश के कोई संकेत नहीं हैं। इसलिए हम आज खेल सकते हैं!'

# Transliterate from Hindi to Telugu
print(UnicodeIndicTransliterator.transliterate(input_text,"hi","te"))
