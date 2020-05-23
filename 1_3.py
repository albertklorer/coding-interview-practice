def convert(string):
    return string.replace(' ', '%20')

assert convert('Mr 3ohn Smith') == 'Mr%203ohn%20Smith'