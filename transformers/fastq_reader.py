def readFastq(filename):
    sequences = []
    qualities = []

    with open(filename, encoding='latin8') as f:
        while True:
            f.readline()
            seq = f.readline().rstrip()
            f.readline()
            qual = f.readline().rstrip()
            if len(seq) == 0:
                break
        
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities
    


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]

    sequences, qualities = readFastq(filename)
    print(len(sequences))