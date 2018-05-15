def mcd(a,b):
    if b == 0:
        return a
    if a == 0:
        return b
    if a>=b:
        mcd(a-b,b)
    if a<b:
        mcd(a,b-a)
    


entrada = 1
lista = []
while (entrada != 0):
    entrada = input('escribe el numero que quiras: ')
    print entrada
    lista.append(entrada)
    print lista
a = lista[1]
b = lista[2]
lista.pop(1)
lista.pop(1)
for i in range (len(lista)):
    c = mcd(a,b)
    a = c
    b = lista[i] 

print c
