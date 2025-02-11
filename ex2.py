def soma_lista_aninhada(arr: list) -> int:
    '''
    Soma os números de uma lista utilizando recursão.
    '''
    if not arr:
        return 0
    
    firstElement = arr[0]
    rest = arr[1:] # resto da lista
    if isinstance(firstElement, list):
        return soma_lista_aninhada(firstElement) + soma_lista_aninhada(rest)
    else:
        return firstElement + soma_lista_aninhada(rest)
        
array = [1, [2, 3], [4, [5]]]   
print(soma_lista_aninhada(array))