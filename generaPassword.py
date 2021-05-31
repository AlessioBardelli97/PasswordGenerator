from random import choices
from sys import argv


if __name__ == '__main__':

    if len(argv) < 2:
        print('Errore: passare la lunghezza della password da generare')
        exit(1)

    length = 0

    try:
        length = int(argv[1])
    except ValueError:
        print('Errore: intero passato non valido')
        exit(1)

    if length <= 0:
        print('Errore: lunghezza non valida')
        exit(1)

    alpha = 'abcdefghikjlmnopqrstuvwxyz'
    ALPHA = alpha.upper()
    digit = '0123456789'
    special = '€£$%&'

    chrs = alpha + ALPHA + digit + special

    tmp = ''.join(choices(chrs, k=length))

    print('Password generata:', tmp)
