def initialize(name):
  c_name = name.title()
  return c_name[0] + "." + c_name[c_name.find(" "):]

def bondify(name):
  c_name = name.title()
  return c_name[c_name.find(" ") + 1:] + ", " + c_name

def piglatin(word):
  constonant = False
  for vowel in ["a", "e", "i", "o", "u"]:
    if word[0].lower() != vowel:
      constonant = True
    else:
      break

  new_word = word
  if constonant:
    new_word = word[1:] + word[0] + "ay"
    for letter in word:
      if letter.isupper():
        new_word = new_word.capitalize()
        break
  else:
    new_word = word + "yay"
    
  return new_word

print(initialize("john doe"))
print(bondify("john doe"))
print(piglatin("fart"))