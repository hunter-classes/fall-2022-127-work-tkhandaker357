def initialize(name):
  c_name = name.title()
  return c_name[0] + "." + c_name[c_name.find(" "):]

def bondify(name):
  c_name = name.title()
  return c_name[c_name.find(" ") + 1:] + ", " + c_name
  
print(initialize("john doe"))
print(bondify("john doe"))