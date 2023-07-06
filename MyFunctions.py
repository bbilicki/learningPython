
# Creating functions - Can do defaults and change order of explictly assigned
def dCountVowels(sentance:str) -> dict:
    """Returns list of vowels found in a sentance""" # doc string
    vowels = set('aeiouy')
    vowel_count = {}

    for ch in list(sentance):
        if ch in vowels:
            vowel_count.setdefault(ch,0)
            vowel_count[ch] += 1

    print(vowel_count)
    return vowel_count


def sFindCommonLetters(sentance:str, letters:str='python') ->set:
    """Return a set of characters common to both arguments"""
    return(set(sentance).intersection(set(letters)))
