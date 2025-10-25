def modulo(x):
    quociente = x / 2
    valor_inteiro = int(quociente) 
    if quociente - valor_inteiro == 0.5:
        resto =  quociente - (quociente - 1)
    else:
        resto = quociente - quociente
    return int(resto)