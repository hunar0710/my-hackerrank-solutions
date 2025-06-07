import itertools

def compress_string(s):
    result = []
    for char, group in itertools.groupby(s):
        count = len(list(group))
        result.append(f"({count}, {char})")
    return " ".join(result)

if __name__ == "__main__":
    s = input().strip()
    print(compress_string(s))
