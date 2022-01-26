def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: Número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial do número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=False))
