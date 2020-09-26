# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 00:37:49 2020

@author: Nikki
"""

import re 
frequency ={}
document_text = open('demo.txt', 'r')
text_string = document_text.read()
match_pattern = re.findall(r'\b[a-zA-Z]{3,15}\b', text_string)
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
#word count of input
frequency_list = frequency.keys()
inp = input("Enter a word:")
try:
    print (inp,":",frequency[inp])
except KeyError:
    print (inp,"is not present in the excerpt")

#all the sentences containing input
from nltk.tokenize import sent_tokenize  
token_text = sent_tokenize(text_string) 
res =[ i for i in token_text if inp in i] 
indx ='\n'.join(res)
print ("\nThe sentences contaning '"+ inp +"'"+" are : \n" + indx)
#conversations containing input

con = re.findall(r'"(?:(?:(?!(?<!\\)").)*)"', str(res))
indx2 ='\n'.join(con)
print ("\nThe conversations contaning '"+ inp +"'"+" are : \n" + indx2)
#count of conversations
count = len(list(filter(lambda x: inp in x, con))) 
print ("\nThe count of conversations contaning '"+ inp +"'"+" are :\n"+str(count))
#All conversations in the excerpt
allconv = re.findall(r'"(.*?)"', str(token_text))
indx3 ='\n'.join(allconv)
print ("\nThe conversations in the excerpt are : \n" + indx3)

from nltk.tag import pos_tag
tagged_sent = pos_tag(text_string.split())
#propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
#print( propernouns)

from nltk.tree import Tree
from nltk import pos_tag, ne_chunk
from nltk.tokenize import SpaceTokenizer
tokenizer = SpaceTokenizer()
toks = tokenizer.tokenize(text_string)
pos = pos_tag(toks)
chunked_nes = ne_chunk(pos) 
nes = [' '.join(map(lambda x: x[0], ne.leaves())) for ne in chunked_nes if isinstance(ne,Tree)]
indx4 ='\n'.join(nes)
print("\n Proper nouns used in the excerpt are:\n", indx4)
