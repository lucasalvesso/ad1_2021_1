import random

def totalPrice(produtos):
    total = 0
    for prods in range(len(produtos)):
        total += float(produtos[prods][2])
    return '{:.2f}'.format(total)

def genMatriz(lojas, produtos):
    result = [['     ']]
    minPrice = [[]] * len(produtos)
    for prod in range(len(produtos)):
        result[0].append(produtos[prod][0])
        minPrice[prod] = [produtos[prod][0]]

    for loja in range(len(lojas)):
        line = [lojas[loja]]

        for prod in range(len(produtos)):
            price = "{:.2f}".format(random.uniform(float(produtos[prod][1]), float(produtos[prod][2])))
            line.append(price)
            if len(minPrice[prod]) == 1:
                minPrice[prod].insert(1, loja)
                minPrice[prod].insert(2, price)
            elif price < minPrice[prod][2]:
                minPrice[prod][1] = loja
                minPrice[prod][2] = price
        result.append(line)

    print('Resultado da pesquisa:')
    for i in result:
        print('     '.join(str(x) for x in i))

    print('\nMenores preços:')
    for prod in minPrice:
        print('{} {}'.format(prod[0], lojas[prod[1]]))

    print('\nValor total: \n R$ {}'.format(totalPrice(minPrice)))

def validInput(val):
    if val >= 0:
        return True
    else:
        return False

L = int(input('Digite o numero de lojas: '))
P = int(input('Digite o numero de produtos: '))

lojas = []
produtos = []

if validInput(L):
    for index in range(L):
        lojas.append(input('Digite o nome da loja: '))

if validInput(P):
    for index in range(P):
        prod = input('Digite o nome do produto: ')
        prod = prod.split(' ')
        if validInput(int(prod[1])) and validInput(int(prod[2])) and int(prod[1]) <= int(prod[2]):
            produtos.append(prod)

genMatriz(lojas, produtos)