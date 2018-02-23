#   This is a program that reads a file
#   Splits the lines of the file into a list
#   Adds unique words to a list and alphabetizes the list of words'

#   create blank list
word_list = []

#   open and read the file
romeo = open('romeo.txt', 'r')

#   for line in file
for lines in romeo:
    lines = lines.rstrip() #get rid of space
    lines = lines.lower() #lowercase
    words = lines.split() #split lines into words
    for word in words: # add unique words to list
        if word not in word_list:
            word_list.append(word)

#   sort words alphabetically
word_list.sort()

#print alphabetized words
for x in word_list:
    print(x)
