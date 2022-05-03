# -*- coding: utf-8 -*-
"""
### Task 1: An English Wordle solver.

There are many strategies to select words that will minimize the number of guesses that a player needs to make: choose a word with as many unguessed letters as possible, to obtain information about each letter; maximize choices to consist of the most common letters; maximize choices to consist of letters in their most frequent positions, etc.

Your task is this.  Given a list of acceptable words in "English_words.txt" (we're changing things up a bit, and giving you words of length *6*, instead of length 5), decide upon a strategy to choose the most likely solution. You are free to use any strategy you want.  

You will likely want to write functions that can:

1. read a list of words into a data structure
2. perform some statistical analysis of the data
3. update the list, given the response of the Wordle game.  All you need to know about the algorithm is that it will accept a suggestion for the word, and will return a list that will correspond to one of the three options cited above.  For example, if the solution is "parse", and you provide "morph", the algorithm will return. [-1,-1,1,0,-1] (ie, the character at position "2" is true, and the one at position "3" is a false position; everything else is a false prediction). You will likely need to make different decisions, depending on the results.  You are *strongly* encouraged to test this functionality thoroughly.
4. If you have guessed the word (ie, the return of the algorithm is [1,1,1,1,1]), then you are done, and you have won the game!  Good job!  If not, then you will need to recalculate the most likely word, given your strategy.

You are free to tackle this problem however you see fit, but here are some strategies that might work:
    * Find common letter distribution patterns (do you want to use extra data?)
    * Find common positional letter distributions
    * Keep track of valid words, and score them according to your statistics, always choosing the most likely one.
    * Choose the one that gives you the most information (not necessarily the same as the previous point).
    * Choose the one that eliminates the most remaining letters.
    * Pick a starting word at random
    * Pick a starting word that is filled with common letters
    * Pick a starting word that has all different letters
    * etc.  Have fun!
"""

# mount google drive
# from google.colab import drive
# drive.mount('/content/drive')

import string
from pathlib import Path
from collections import Counter
from itertools import chain
import operator

# here change the path of the English dictionary
DICT = "/Users/lxy/Downloads/English6.txt"

# allowable characters to be in the set of ascii letters
ALLOWABLE_CHARACTERS = set(string.ascii_letters)

# maximum attempts to be 6, otherwise task failed
ALLOWED_ATTEMPTS = 6

# word length is 6
WORD_LENGTH = 6

# create the WORDS dictionary from the DICT
WORDS = {
  word.lower()
  for word in Path(DICT).read_text().splitlines()
  if len(word) == WORD_LENGTH and set(word) < ALLOWABLE_CHARACTERS
}

# make the WORDS dict a counter
LETTER_COUNTER = Counter(chain.from_iterable(WORDS))

# create the LETTER_FREQ to faciliate the word choosing process
LETTER_FREQUENCY = {
    character: value / sum(LETTER_COUNTER.values())
    for character, value in LETTER_COUNTER.items()
}

def calculate_word_commonality(word):
    """
      rule for choosing the word: Since a string is an iterable by iterating 
      over every character in the word, we can get the frequency of each word 
      and add it up; 
      the total tally is then divided by the word length minus the number of 
      unique characters (plus one, to prevent division of zero).
    """
    score = 0.0
    for char in word:
        score += LETTER_FREQUENCY[char]
    return score / (WORD_LENGTH - len(set(word)) + 1)

def sort_by_word_commonality(words):
    """
      generate a sorted (highest-to-lowest) list of tuples, 
      with each tuple containing the word and the calculated score for that word. 
      The key we are sorting on is the score.
    """

    sort_by = operator.itemgetter(1)
    return sorted(
        [(word, calculate_word_commonality(word)) for word in words],
        key=sort_by,
        reverse=True,
    )

def display_word_table(word_commonalities):
    """
      to display our top 5 word choices every time
    """
    for (word, freq) in word_commonalities:
        print(f"{word:<5} | {freq:<5.2}")

def input_word():
    """
      let the user input the choosed words
    """
    while True:
        word = input("Input the word you entered> ")
        if len(word) == WORD_LENGTH and word.lower() in WORDS:
            break
    return word.lower()


def input_response():
    """
      to gather the response of the golden rule
    """
    print("Type the color-coded reply from Wordle:")
    print("  G for Green: correct letter")
    print("  Y for Yellow: letter in the sequence but wrong position")
    print("  ? for Gray: wrong guess, not in the word")
    while True:
        response = input("Response from Wordle> ")
        if len(response) == WORD_LENGTH and set(response) <= {"G", "Y", "?"}:
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
    assert len(word) == len(word_vector)
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


def solve():
    possible_words = WORDS.copy()
    word_vector = [set(string.ascii_lowercase) for _ in range(WORD_LENGTH)]
    for attempt in range(1, ALLOWED_ATTEMPTS + 1):
        print(f"Attempt {attempt} with {len(possible_words)} possible words")
        display_word_table(sort_by_word_commonality(possible_words)[:15])
        word = input_word()
        response = input_response()
        if response == 'G' * WORD_LENGTH:
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


if __name__ == "__main__":
    solve()



"""
what we could expect from solve:

1. it will show you all the possible words from our list ranked by probabilities
2. choose a word that you are going to use (it should be the highest ranking one in most cases)
3. return the color-coded reply from Wordle
4. our system will automatically calculate the next possible word for you
"""

