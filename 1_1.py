# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures? 

def check(string):
    s = set()
    for char in string:
        if char in s:
            return False
        s.add(char)

    return True

assert check('aaaaaaa') == False
assert check('al th!^&') == True
assert check('abcdeh') == True
assert check('') == True
