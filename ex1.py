def reverter_caracteres(string: str) -> str:
    '''
    Inverte a string utilizando recursão.
    '''
    if len(string) <= 1:
        return string
    else:
        return reverter_caracteres(string[1::]) + string[0]
    
print(reverter_caracteres('welcome'))