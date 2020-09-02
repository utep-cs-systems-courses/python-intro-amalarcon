# -*- coding: utf-8 -*-
"""
This program takes in an input file and creates
an output file of every word in the input file
along with occurences of it
@author: Aaron
@since: Sepetember 1, 2020
"""

import sys        # command line arguments
import string     # easy punctuation 
import re         # regular expression tools
import os         # checking if file exists

#Check for input arguments
if len(sys.argv) != 3:
    print(sys.argv)
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()
 
#get sys variables and establish dictionary 
inp = sys.argv[1]
out = sys.argv[2]
diction = dict()
    
#make sure text file exists
if not os.path.exists(inp):
    print ("text file input %s doesn't exist! Exiting" % inp)
    exit()

#open file
with open(inp, "r") as inputfile:
    #process text while removing punctuation
    translator = str.maketrans('','',string.punctuation)
    inArr = re.sub("-|'", " ", inputfile.read()).translate(translator).lower().split()
    
    #for every word, increment its count in the dictionary
    for word in inArr: 
        if word in diction:
            diction[word] +=1
        else:
            diction[word] = 1
  
#print out results          
with open(out, "w") as outputfile:
    for word, occ in sorted(diction.items()):
        outputfile.write("%s %s\n" % (word, str(occ)))
        
    