# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

def check(string):
    # build dictionary from string
    dictionary = {}
    for char in string:
        if char in dictionary:
            dictionary[char] = dictionary[char] + 1
        else:
            dictionary[char] = 1

    # iterate through dictionary couting
    flag = False
    for key in dictionary.keys():
        # even
        if dictionary[key] % 2 == 1 and flag == True:
            flag = False

        # uneven
        elif dictionary[key] % 2 == 1 and flag == False:
            flag = True

    if len(string) % 2 == 0 and flag == True:
        return False

    elif len(string) % 2 == 0 and flag == False:
        return True

    elif len(string) % 2 == 1 and flag == True:
        return True

    else:
        return False


assert check('tactcoa') == True
