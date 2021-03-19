L1=[1,2,3,4]
def multi(lista):
    product=1
    for element in lista:
        product = product * element
    return product

print (multi(L1))