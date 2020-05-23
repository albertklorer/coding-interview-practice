# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away. 

def check(str1, str2):
    dic1 = {}
    dic2 = {}

    # iterate through dic1 and get characer counts
    for char in str1:
        if char in dic1:
            dic1[char] = dic1[char] + 1
        else:
            dic1[char] = 1
            dic2[char] = 0

    # iterate through dic2 and get character counts
    for char in str2:
        if char in dic2:
            dic2[char] = dic2[char] + 1
        else:
            dic2[char] = 1
            
            if dic2[char] not in dic1:
                dic1[char] = 0

    # get absolute difference between dictionaries
    difference = 0 
    for key in dic1.keys():
        difference = difference + (abs(dic1[key] - dic2[key]))

    # return false in case where differences exceed the edit allowed
    if difference > 2:
        return False

    return True

assert check('pales', 'pale') == True
assert check('pale', 'bale') == True
assert check('pale', 'bake') == False