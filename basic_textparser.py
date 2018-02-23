def main():
    file_name = input('File Name:')

    open_file = open(file_name, 'r')
    counts = dict()

    parse_text(open_file, counts)

    for key in counts:
        print(key, counts[key])

def parse_text(open_file, counts):
    for line in open_file:
        line = line.rstrip()
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] = counts[word] + 1

    return counts

main()
