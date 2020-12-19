from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator
input_text='राजस्थान'
# input_text='രാജസ്ഥാന'
# input_text='රාජස්ථාන'
print(UnicodeIndicTransliterator.transliterate(input_text,"hi","kn"))
