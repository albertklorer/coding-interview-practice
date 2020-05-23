# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other. 

def check(str1, str2):
    dic1 = {}
    dic2 = {}

    # build dictionary character by character
    for char in str1:
        if char in dic1:
            dic1[char] = dic1[char] + 1

        else:
            dic1[char] = 1

    # build dictionary character by character
    for char in str2:
        if char in dic2:
            dic2[char] = dic2[char] + 1

        else:
            dic2[char] = 1

    # check equality of dictionaries
    if dic1 == dic2:
        return True

    return False

assert check('aaabbr', 'baabra') == True
assert check('', '') == True
assert check('aa', 'aa') == True
assert check('aa!!Aa', 'a!') == False

