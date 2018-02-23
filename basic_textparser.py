def main():
    file_name = input('File Name:')

    open_file = open(file_name, 'r')
    counts = dict()
    stopwords = ['the','and', 'he','they', 'in', 'as', 'was', 'for', 'by', 'a', 'it', 'at']

    parse_text(open_file, counts,stopwords)

    for key in counts:
        print(key, counts[key])

def parse_text(open_file, counts, stopwords):
    for line in open_file:
        line = line.rstrip()
        line = line.lower()
        words = line.split()
        for word in words:
            if word in stopwords:
                continue
            else:
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] = counts[word] + 1

    return counts

main()
