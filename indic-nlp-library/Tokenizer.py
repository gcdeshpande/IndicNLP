from indicnlp.tokenize import indic_tokenize  

indic_string='सुनो, कुछ आवाज़ आ रही है। फोन?'

print('Input String: {}'.format(indic_string))
print('Tokens: ')
for t in indic_tokenize.trivial_tokenize(indic_string): 
    print(t)
