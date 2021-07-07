def countContigs(filename):
    headers = []

    with open(filename, encoding='latin8') as f:
        for line in f:
            if line.startswith(">"):
                headers.append(line)
    return headers
    


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]

    headers = countContigs(filename)
    print(len(headers))