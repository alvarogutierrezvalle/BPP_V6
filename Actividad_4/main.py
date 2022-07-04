import pdb
pdb.set_trace()


# Uso de la Comprensión de Listas
listas = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

def max_listas(mis_listas):
    maximos=[max(i) for i in mis_listas]
    return maximos


# Uso de la función Filter
def es_primo(n):
    primo = True
    for i in range(2, n):
        if(n%i == 0):
            primo = False
    return primo

numeros = [3, 4, 8, 5, 5, 22, 13]

primos = list(filter(es_primo, numeros))

print("Los números primos de la lista es:",primos)

if __name__ == '__main__':
    max_listas(listas)