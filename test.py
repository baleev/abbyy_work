import nltk
text = '"Всё, что ни делается, - к лучшему!" - сказал я.'
list1 = nltk.tokenize.sent_tokenize(text, language='russian')
print(list1)
'''
print(nltk.download())'''