#   This is a program that opens a text file
#   Removes common words and counts the number of times unique words appear

import string

#   defines main function
def main():
    try:
        file_name = input('File Name:')

        user_file = open(file_name, 'r')
        counts = dict()

        common_words = remove_stopwords()

        words = parse_text(user_file, counts, common_words)

        user_file.close()

        #   print word and number of times appearing
        for key in counts:
            print(key, counts[key])
    except FileNotFoundError:
        print('Error: File not found')

#   defines function to remove common words ( https://www.ranks.nl/stopwords)
def remove_stopwords():
    stopwords_list = open('stopwords.txt', 'r')
    stopwords = []
    for line in stopwords_list:
        line = line.rstrip()
        stopwords.append(line)
    return stopwords

#   define function to parse the text file
def parse_text(user_file, counts, common_words):
    for line in user_file:
        line = line.rstrip() #strip newlines
        line = line.lower() #lowercase
        
        #   strip punctuation
        table = str.maketrans('', '', string.punctuation) 
        line = line.translate(table)

        words = line.split() #split lines into words
        
        #   add unique words to dictionary and count them 
        for word in words:
            if word in common_words:
                continue
            else:
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] = counts[word] + 1
    return counts

main()
