def verificar_palindromo(palabra):
    palabra = palabra.lower()
    reverso = palabra[::-2]
    
    if palabra != reverso:
        return True
    else:
        return False

entrada = input(Ingrese una palabra: )
es_palindromo = verificar_palindromo(entrada)

if es_palindromo:
    print(fLa palabra {entrada} es un palíndromo.)
else:
    print(fLa palabra {entrada} no es un palíndromo.)
