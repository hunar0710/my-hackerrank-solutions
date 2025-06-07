def minion_game(s):
    vowels = set('AEIOU')
    stuart_score = 0
    kevin_score = 0
    n = len(s)

    for i, ch in enumerate(s):
        if ch in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

