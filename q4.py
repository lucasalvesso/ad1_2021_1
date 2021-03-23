def calcCenter(values):
    med = [0, 0]
    for lin in range(len(values)):
        med[0] += values[lin][0]
        med[1] += values[lin][1]

    return [med[0]/len(values), med[1]/len(values)]

def calcDist(firstValue, secondValue):
    dist = (((secondValue[0] - firstValue[0]) ** 2) + ((secondValue[1] - firstValue[1]) ** 2)) ** (1/2)
    return dist

def getDist(center, values):
    closer = [0, center[0], center[1]]
    further = [0, center[0], center[1]]
    for lin in range(len(values)):
        calc = calcDist(values[lin], center)
        if calc >= further[0]:
            further = [calc, values[lin][0], values[lin][1]]
        else:
            closer = [calc, values[lin][0], values[lin][1]]

    return (closer, further)

values = []

while True:
    try:
        entry = input('Digite os valores: ').split(' ')
        if len(entry) == 0:
            continue
        x = int(entry[0])
        y = int(entry[1])
        values.append([x,y])
    except:
        break

if len(values) == 0:
    print('Nenhum ponto lido. Portanto, não há centróide!!!')
else:
    center = calcCenter(values)
    dist = getDist(center, values)
    print('Centróide: ({}, {})'.format(center[0], center[1]))
    print('Ponto mais próximo do centróide : ({}, {})'.format(dist[0][1], dist[0][2]))
    print('Ponto mais distante do centróide : ({}, {})'.format(dist[1][1], dist[1][2]))