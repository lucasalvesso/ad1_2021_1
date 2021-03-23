def getDiff(word1, word2):
    totalDiff = 0
    cases = []
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            totalDiff += 1
            cases.append(i)
    return [totalDiff, cases]

def getSubs(motif, dna, hamming):
    for sub in range(len(dna)):
        if sub <= (len(dna) - len(motif)):
            string = dna[sub:(len(motif) + sub)]
            diff = getDiff(motif, string)

            if diff[0] <= hamming:
                print('{} {}'.format(sub + 1, ' '.join(str(x + 1) for x in diff[1])))

k = int(input('Distância de Hamming: '))
if int(k) and k > 0 and k <= 50:
    s = input('Motif: ')
    if len(s) <= 50:
        t = input('Dna: ')
        if len(t) <= 500:
            print('As substrings com distância no máximo {} do mofit e as posições são: \n'.format(k))
            getSubs(s, t, k)
        else:
            print('Valores não estão de acordo')
    else:
        print('Valores não estão de acordo')
else:
    print('Valores não estão de acordo')