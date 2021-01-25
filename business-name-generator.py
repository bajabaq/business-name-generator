#
#This is a silly simple script to create a business name
#or other entity name
#
#usage:  python3 business-name-generatory.py [business-type] [num-names]
#output: random-adjective random-noun [business-type]  (1 line for num-names)
#
#example: python3 business-name-generatory.py realty 
#         blue dog realty
#
#

import random
import sys

def get_random_word(word_type):
    if word_type == "adjective":
        fname = "28K-adjectives.txt"
    elif word_type == "noun":
        fname = "91K-nouns.txt"
    #endif
    with open(fname,"r") as fh:
        words = [line.strip() for line in fh.readlines()]
    #endwith
    word = random.choice(words)
    return word
#enddef

def get_adjective():
    word = get_random_word("adjective")
    return word
#enddef

def get_noun():
    word = get_random_word("noun")
    return word
#enddef

if __name__ == "__main__": 
    num_args  = len(sys.argv)
    if num_args == 2:
        entity = sys.argv[1]
        num_names = 1
    elif num_args == 3:
        entity    = sys.argv[1]
        try:
            num_names = int(sys.argv[2])
        except:
            print("must be an integer")
            num_names = 1
        #endtry
    else:
        entity = ""
        num_names = 1
    #endif
    for i in range(num_names):
        adjective = get_adjective()
        noun      = get_noun()
        print(i,") ",adjective,noun,entity)
    #endfor

#endif
