'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    ss = 'th'
    length = len(word)
    lss = len(ss)

    if length == 0 or length < lss: #edge cases
        return 0
    if word[0:lss] == ss: #base case - for index 0 through the substring (ss) length, where we find the substring ->
        return count_th(word[lss-1:]) + 1 #add +1 when SS is found, and run through this recursively again. 

    return count_th(word[lss-1:]) #return count when ss is no longer found in the recursive function
    
