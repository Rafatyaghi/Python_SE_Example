import re, timeit
from collections import namedtuple

RegEx = namedtuple("regEx", "title pattern")
allRegEx = [RegEx(" 1. Email accounts  : ", "[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]*[@]\w+[.]\w+[.]?\w+"),
            RegEx(" 2. Dates : ", "((3[0-1]|2[0-9]|1[1-9]|0?[1-9])\s?(/|:|-)\s?(1[0-2]|0?[1-9])\s?(/|:|-)\s?[0-9]{4})"),
            RegEx(" 3. Phones No : ", "(([+]?(97(0|2)|0))?(-|:|\s)*?\d{2}(-|:|\s)*?\d{3}(-|:|\s)*?\d{4})"),
            RegEx(" 4. Quoted Strings", "(\"[^\"]*\")"),
            RegEx(" 5. Float Numbers", "[+-]?[0-9]*[.][0-9]+"),
            RegEx(" 6. Some Files Extension", ".*[.](cpp|doc|py|jpg|gif|pdf)"),
            RegEx(" 7. IPv6 Addresses", "(([0-9a-fA-F]{4}:){3}[0-9a-fA-F]{4})"),
            RegEx(" 8. String consist of only vowels", "\\b[aeiuo]+\\b"),
            RegEx(" 9. Multiples of Five", "\\b([0-9]*(0|5))\\b"),
            RegEx("10. Words begins and end with 'a'", "\\ba\w*?a\\b")]

for currentRegEx in allRegEx:

    txtFile = open('file.txt', 'r')
    start = timeit.default_timer()
    matches = re.findall(currentRegEx.pattern, txtFile.read())
    #matches = re.sub()
    stop = timeit.default_timer()
    print(currentRegEx.title, 
        '\n================================='
        '\nNumber of matches: ', len(matches), 
        '\nMatches: ', matches,
        '\nRuntime: (', stop - start, ')sec',
        '\n\n\n')