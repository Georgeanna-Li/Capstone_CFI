# -*- coding: utf-8 -*-

"""### Task 2: A Gitksan Wordle solver.

Gitksan is the language of the Gitxsan people of British Columbia.  It belongs to the Tsimshianic language family, and has far fewer speakers than English.  The traditional territories consist of 50,000 square km in the Skeena river watershed (pictured below).  The language is written using a modified version of the Latin alphabet, with both digraphs/trigraphs (two/three letters that represent one sound, like 'th' in English) and diacritics (accents or markings that change the meaning of the letter).  For example, "hl" is considered one letter, representing a single sound, as is <ins>k</ins>.  The letters used in Gitksan are as follow (sourced from : Gitksan, by Jason Brown, Henry Davis, Michael Schwan and Barbara Sennott).  Thanks to the Gitksan Lab in the UBC department of Linguistics for providing the dictionary, and being very enthusiastic about this coding problem.  
<img src="img/Skeena_river_basin_map.png" alt="Traditional Gitxsan territory" width="200"/>

p
b
d
t
k
kw
<ins>k</ins>
gy
gw
<ins>g</ins>
ts
j
p'
t'
ky'
kw'
<ins>k</ins>'
ts'
tl'
m
n
s
x
xw
<ins>x</ins>
h
hl
y
w
l
'm
'n
'l
'y
'w
i
ii
ee
a
aa
oo
u
uu

Now, you will need to add an additional step of breaking your words into characters, and recalculating your statistics based on those letters.  'laaxw' ("trout") is not [l, a, a, x, w], but rather, [l, aa, xw].  You will have to modify your code so that it accepts lists of characters instead of words.  In the provided 'Gitksan5.txt' file, underlined characters are represented with a following underscore: _. So <ins>x</ins> is x_, <ins>k</ins>' is k_', etc.  You will have to determine your own way of segmenting the data to represent Gitksan letters.
    
Here are some hints and tips (courtesy of Michael Schwan in the Gitksan lab):
    
    * A sequence of something like k_' = ḵ'
      Underlines only apply to k g and x (phonetically, they represent a uvular version of their velar equivalent.  ELI5: your tongue is farther back in your mouth when you pronounce them.)

    * An apostrophe between two vowels is a glottal stop (like the sound in "uh-oh")
    
    * An apostrophe before m n l y or w is a "glottalized resonant" and goes before the resonant, so 'm 'n 'l 'y and 'w (no English equivalent, but it's a bit like a little cough or hiccough as you pronounce the sound)
    
    * An apostrophe after a stop or affricate is a glottalized obstruent (not necessarily ejective), p' t' ts' tl' k' ky' kw' ḵ' (again, no English equivalent, but they sound notably different from similar sounds in English).

    * Digraphs to look out for are xw kw gw ky gy ts hl, and kw ky and ts can be followed by an apostrophe (tl' is only ever glottalized. tl without apostrophe is just a sequence of t and l).  If you're interested, the "w" digraphs are prounounce with the lips rounded, and the "y" ones with the middle of the tongue raised towards the roof of the mouth).

    * Long vowels are also digraphs. e = short /e/, and ee = long /e:/
    
    
There may be instances where you have to make a choice in how a word is segmented, and it may impact your results slightly.  It would take a certain level of fluency in Gitksan to always get this correct, but don't worry - consistency is more important than 100% accuracy.

### Evaluation

Just as with the English solver, we will evaluate on a set of words, and the team with the lowest average number of guesses will win a bonus percentage point.  The team in second place will win a half a percentage point.  This applies to both parts - theoretically, one team could win 2 percentage points.

Since we only have limited data for Gitksan, we will consider one of the largest subsets within the data - words of 5 characters.  We are counting digraphs / trigraphs as 1 character, and the space is also 1 character.  There are ~200 5 "letter" words in the data set - we will evaluate on a random selection of 100 of them.
"""
from pathlib import Path
import string
from collections import Counter
from itertools import chain
import operator

GIT_WORD_LENGTH = 5
ALLOWED_ATTEMPTS = 6
#Change to your local directory
DICT = 'Gitksan5.txt'
with open(DICT, encoding = 'utf-8') as f:
    gitksan_word_list = [i.strip('\n').split('\t')[0] for i in f.readlines()]
token_str = "p b d t k kw k_ gy gw g_ ts j p' t' ky' kw' k_' ts' tl' m n s x_ xw x h hl y w l 'm 'n 'l 'y 'w i ii ee a aa oo u uu . e o g k' s'"
token_list = token_str.split()
# An apostrophe between two vowels 
vowels = 'aeiou'
for i in vowels:
    for j in vowels:
        token_list.append(i+"'"+j)
special_tokens=[]
token_list.append(' ')
for i in vowels:
    for j in vowels:
        special_tokens.append(i*2+"'"+j)
        
def find_tokens(word, tokens):
    """
        this function begins by checking whether the first four symbols are an existing token,
        if no, we move on to the first three, and then the first two. 
    """
    #word = word.replace(' ', '')
    #####
    if word[:4] in special_tokens:
      tokens.append(word[0])
      tokens.append(word[1:4])
      word = word[4:]
    #####
    if word[:3] in token_list:
        tokens.append(word[:3])
        word = word[3:]
        find_tokens(word, tokens)
    elif word[:2] in token_list:
        tokens.append(word[:2])
        word = word[2:]
        find_tokens(word, tokens)
    elif word[:1] in token_list:
        tokens.append(word[:1])
        word = word[1:]
        find_tokens(word, tokens)
    return tokens

# creat gitxsan counter for the words
GITXSAN_COUNTER = Counter()
for word in gitksan_word_list:
  for token in find_tokens(word, []):
    GITXSAN_COUNTER[token] += 1

# create the letter frequency
GITXSAN_LETTER_FREQUENCY = {
    character: value / sum(GITXSAN_COUNTER.values())
    for character, value in GITXSAN_COUNTER.items()
}

def calculate_word_commonality_git(word):
    """
      rule for choosing the word: Since a string is an iterable by iterating 
      over every character in the word, we can get the frequency of each word 
      and add it up; 
      the total tally is then divided by the word length minus the number of 
      unique characters (plus one, to prevent division of zero).
    """
    score = 0.0
    for char in find_tokens(word,[]):
      score += GITXSAN_LETTER_FREQUENCY[char]
    return score/ (GIT_WORD_LENGTH - len(find_tokens(word,[])) + 1)

def sort_by_word_commonality_git(words):
    """
      generate a sorted (highest-to-lowest) list of tuples, 
      with each tuple containing the word and the calculated score for that word. 
      The key we are sorting on is the score.
    """
    sort_by = operator.itemgetter(1)
    return sorted(
        [(word, calculate_word_commonality_git(word)) for word in words],
        key=sort_by,
        reverse=True,
    )

def input_word_git():
    """
      let the user input the choosed words
    """
    while True:
        word = input("Input the word you entered> ")
        if len(find_tokens(word,[])) == GIT_WORD_LENGTH and word.lower() in gitksan_word_list:
            break
    return find_tokens(word,[])

def input_response_git():
    """
      to gather the response of the golden rule
    """
    print("Type the color-coded reply from Wordle:")
    print("  G for Green")
    print("  Y for Yellow")
    print("  ? for Gray")
    while True:
        response = input("Response from Wordle> ")
        if response == "G" * GIT_WORD_LENGTH:
          break
        if len(response) == GIT_WORD_LENGTH and set(response) <= {"G", "Y", "?"}:
            break
        else:
            print(f"Error - invalid answer {response}")
    return response

def match_word_vector(word, word_vector):
    """
      function that returns if a word matches the word vector.
      uses zip to pairwise match each character in the word, 
      and each character in the word vector (if any)

      If the letter is not in the word vector set at that position, 
      exit with a failed match. 
      Otherwise, proceed and, if we exit the loop naturally, 
      return True indicating a match.
    """
    # assert len(word) == len(word_vector)
    for letter, v_letter in zip(word, word_vector):
        if letter not in v_letter:
            return False
    return True

def match(word_vector, possible_words):
    """
      merges the concepts into a single list comprehension that does the checking. 
      Each word is tested against word_vector with match_word_vector.
    """
    return [word for word in possible_words if match_word_vector(word, word_vector)]

def display_word_table(word_commonalities):
    """
      to display our top 5 word choices every time
    """
    for (word, freq) in word_commonalities:
        print(f"{word:<5} | {freq:<5.2}")

def solve_git():
    possible_words = set(gitksan_word_list).copy()
    word_vector = [set(token_list) for _ in range(GIT_WORD_LENGTH)]
    for attempt in range(1, ALLOWED_ATTEMPTS + 1):
        print(f"Attempt {attempt} with {len(possible_words)} possible words")
        display_word_table(sort_by_word_commonality_git(possible_words)[:15])
        word = input_word_git()
        response = input_response_git()
        if response == 'G' * GIT_WORD_LENGTH:
          print("success!")
          break
        for idx, letter in enumerate(response):
            if letter == "G":
                word_vector[idx] = {word[idx]}
            elif letter == "Y":
                try:
                    word_vector[idx].remove(word[idx])
                except KeyError:
                    pass
            elif letter == "?":
                for vector in word_vector:
                    try:
                        vector.remove(word[idx])
                    except KeyError:
                        pass

        possible_words = match(word_vector, possible_words)

if __name__ == '__main__':
    solve_git()
