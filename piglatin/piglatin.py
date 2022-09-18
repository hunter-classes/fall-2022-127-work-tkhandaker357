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
            
  for vowel in ["a", "e", "i", "o", "u"]:
    if word[0].lower() == vowel:
      new_word = word[1:] + word[0] + "ay"
  if new_word == word:
    new_word = word + "yay"

  if allcaps:
    new_word = new_word.upper()
  elif word[0].isupper():
    new_word = new_word.capitalize()

  return new_word

print(initialize("john doe"))
print(bondify("john doe"))
print(piglatin("aLAbAmA"))