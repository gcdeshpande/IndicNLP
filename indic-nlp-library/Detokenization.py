from indicnlp.tokenize import indic_detokenize  
indic_string='" सुनो , कुछ आवाज़ आ रही है . " , उसने कहा । '

print('Input String: {}'.format(indic_string))
print('Detokenized String: {}'.format(indic_detokenize.trivial_detokenize(indic_string,lang='hi')))
