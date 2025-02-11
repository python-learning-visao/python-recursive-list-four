def contar_caracteres(string:str, caracter:str) -> int:
    '''
    Conta o número de caracteres em uma string utilizando recursão.
    '''
    if not string:
        return 0

    elif string[0] == caracter:
        return 1 + contar_caracteres(string[1:], caracter)
    
    else: 
        return contar_caracteres(string[1:], caracter) 

rst = contar_caracteres('banana', 'a')

print(rst)