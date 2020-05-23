# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z). 

def compress(string):
    # add null terminator to string
    string = string + '\0'

    # declare variables
    compressed_string = ''
    char = None
    count = 0
    i = 0

    # iterate for length of string
    while (i < len(string)):
        if char == None:
            char = string[i]
            count = count + 1

        elif char == '\0':
            compressed_string = compressed_string + str(char) + str(count)
            break

        elif char == string[i]:
            count = count + 1

        elif char != string[i]:
            compressed_string = compressed_string + str(char) + str(count)
            count = 1
            char = string[i]

        i = i + 1
    
    # check for length of compressed string
    if len(string) < len(compressed_string):
        return False

    return compressed_string

assert compress('aabcccccaaa') == 'a2b1c5a3'
assert compress('abcdef') == False