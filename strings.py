def linha(tam=50):
    print('-' * tam)

def cabecalho(txt, tam=50):
    linha(tam)
    print(txt.center(tam))
    linha(tam)

def pausar():
    input('Pressione ENTER para continuar...')