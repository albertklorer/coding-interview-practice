# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.) 

def convert(string):
    return string.replace(' ', '%20')

assert convert('Mr 3ohn Smith') == 'Mr%203ohn%20Smith'