import re

def cleanprogramcd(siscd):
    cleanedcd = re.sub( r'[^\x00-\x7F]+', '', siscd)
    if cleanedcd[-1].isnumeric:
        cleanedcd = cleanedcd[:-1]
    else:
        cleanedcd = cleanedcd
    return cleanedcd