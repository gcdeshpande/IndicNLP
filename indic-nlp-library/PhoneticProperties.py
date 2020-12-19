from indicnlp.langinfo import *

c='क'
lang='hi'

print('Is vowel?:  {}'.format(is_vowel(c,lang)))
print('Is consonant?:  {}'.format(is_consonant(c,lang)))
print('Is velar?:  {}'.format(is_velar(c,lang)))
print('Is palatal?:  {}'.format(is_palatal(c,lang)))
print('Is aspirated?:  {}'.format(is_aspirated(c,lang)))
print('Is unvoiced?:  {}'.format(is_unvoiced(c,lang)))
print('Is nasal?:  {}'.format(is_nasal(c,lang)))
