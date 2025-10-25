def modulo(numero):
    resto = numero / 2
    absoluto = int(resto) 
    if resto - absoluto == 0.5:
        modulo =  resto - (resto - 1)
    else:
        modulo = resto - resto
    return int(modulo)
numero = int(input('Digite um número: '))
resto = modulo(numero)
print(f"Resto é igual a {resto}")