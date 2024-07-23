def soma(x, y):
    '''soma x e y

    >>> soma(10, 20)
    30
    >>> soma(-10, 20)
    10
    >>> soma(10, 10)
    20
    '''
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'x precisa ser int ou float'
    return x + y

def subtrai(x, y):
    '''Subtrai x e y

    >>> subtrai(10, 5)
    5
    >>> subtrai('10', 5)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    '''
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'x precisa ser int ou float'
    return x - y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
