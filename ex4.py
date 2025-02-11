def indice_maior_elemento(lista: list, index: int=0, maior_index: int=0) -> int:
    '''
    Analisa uma lista e retorna o índice do maior valor presente nela.
    '''
    # Caso a lista esteja vazia, retorna o index do maior elemento
    if index >= len(lista):
        return maior_index
    
    # Compara o elemento atual com o maior encontrado
    if lista[index] > lista[maior_index]:
        maior_index = index  # Atualiza o index do maior elemento
    
    # Chamada recursao para o próx index
    return indice_maior_elemento(lista, index + 1, maior_index)

rst = indice_maior_elemento([1, 5, 3, 9, 2, 200, 23, 1202]) # >>>>>>>>> 
print(rst) 