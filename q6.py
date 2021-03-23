def palind(val):
    if val[0] == val[-1] and len(val) > 2:
        return palind(val[1:-1])
    elif val[0] == val[-1] and len(val) <= 2:
        return True
    else:
        return False

words = []

while True:
    try:
        entry = input('Digite a palavra: ')
        if len(entry) == 0:
            break
        words.append(entry)
    except:
        break

for word in words:
    if palind(word):
        print(word)