from hashlib import new
from string import punctuation, whitespace

def initialize(name):
  c_name = name.title()
  return c_name[0] + "." + c_name[c_name.find(" "):]

def bondify(name):
  c_name = name.title()
  return c_name[c_name.find(" ") + 1:] + ", " + c_name

def piglatin(word):
  new_word = word
  allcaps = False
  for letter in word:
    if letter.isupper():
      allcaps = True
    else:
      allcaps = False
      break

  punctuation_mark = ''
  if word[-1] in ['.', '!', '?']:
    punctuation_mark = word[-1]
    word = word.replace(punctuation_mark, '')
    new_word = word

  for letter in word:
    if letter in ['a', 'e', 'i', 'o', 'u']:
      new_word = word[1:] + word[0] + "ay"
  if new_word == word:
    new_word += "yay"

  new_word += punctuation_mark

  if allcaps:
    new_word = new_word.upper()
  elif word[0].isupper():
    new_word = new_word.capitalize()

  return new_word
