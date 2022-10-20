file = open("stuff.dat")

data = file.read()
print(data)

paragraphs = data.split("\n\n")
for index in range(len(paragraphs)):
    paragraphs[index] = paragraphs[index].split()
    paragraphs[index] = ' '.join(paragraphs[index])

print(paragraphs[0])