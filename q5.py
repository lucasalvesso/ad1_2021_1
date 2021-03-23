def countNullVotes(blank, candidates, votesLength):
    total = votesLength - blank
    for cand in candidates:
        total -= int(cand[2])
    return total

def getVotes (candidates, votes):
    candidates_votes = []
    for cand in candidates:
        candidates_votes.append([cand[0], cand[1], votes.count(cand[1])])
    return candidates_votes

candidates = []
votes = []
total_cand = input('Quantidade de candidatos: ')
for i in range(int(total_cand)):
    cand = ''
    while True:
        try:
            cand = input('Candidato: ').split('#')
        except:
            continue

        if (int(cand[1]) < 1):
            print('Número inválido. Digite novamente')
            continue
        else:
            candidates.append([cand[0], cand[1], 0])
            break

while True:
    try:
        entry = int(input('Voto: '))
        if int(entry) < 0:
            continue
        votes.append(entry)
    except:
        break
total_votes = getVotes(candidates, votes)
blank = votes.count(0)
null = countNullVotes(blank, total_votes, len(votes))
for cand in total_votes:
    print('{} - {} - com {} voto(s)'.format(cand[0], cand[1], cand[2]))

print('Brancos - com {} voto(s)'.format(blank))
print('Nulos - com {} voto(s)'.format(null))