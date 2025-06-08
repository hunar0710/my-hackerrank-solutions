def word_order():
    n = int(input().strip())
    words = input().strip().split()

    counts = {}     
    order = []      

    for w in words:
        if w not in counts:
            counts[w] = 0
            order.append(w)
        counts[w] += 1

    print(len(order))
    print(' '.join(str(counts[w]) for w in order))


if __name__ == '__main__':
    word_order()
