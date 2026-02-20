def fatorial(numero, mostrar=False):
    f=1
    for c in range(numero, 0, -1):
        f*=c
        if mostrar==True:
            if c>1:
                print(f'{c} X ', end='')
            else:
                print(f'{c} = ', end='')
    return f

def dobro(numero):
    return numero*2

def triplo(numero):
    return numero*3

def raiz(numero):
    return numero**(1/2)

def leiaInt(msg):
    while True:
        try:
            i=int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
        else:
            break
    return i

def moeda(num=0, moeda='R$'):
    n=float(num)
    return f'{moeda}{n:.2f}'.replace('.', ',')

