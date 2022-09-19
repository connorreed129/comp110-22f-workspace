"""Example implementing a list utility function. """
#two parameters: needle(str) and haystack(list[str]
#return type bool:
def contains(needle:str, haystack: list[str])-> bool:
    """finding a word in a list of words. """
    i=0
    while i<len(haystack):
       if haystack[i] == needle:
        return True 
        i+=1
    return False 

#gameplan:
#1. start with first index
#2 loop through every index
 #2.A Test if item at index is equal to needle
 #2B True retrin true! we found it!
 #3 Return false