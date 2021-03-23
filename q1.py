import math

def calc(values):
    pi = "{:.3f}".format(math.pi)
    dist = values[0] * 100000
    comp = (values[1]/2) * 2 * float(pi)
    total = dist / comp
    n = len(str(int(total // 1))) - 1

    if (total / n) >= 3.16:
        n += 1

    return n

values = [0, 0]

for index in range(len(values)):
    values[index] = int(input('Digite o valor: '))

operation = calc(values)

print("Distância percorrida: {} km".format(values[0]))
print("Diâmetro da roda: {} cm".format(values[1]))
print("Ordem de grandeza da quantidade de voltas efetuadas: {} elevado a {}".format(10, operation))