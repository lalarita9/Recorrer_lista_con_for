"""
Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for, e 
imprimir en pantalla el valor de cada elemento indicando si es par, impar o cero.
"""
num= [5,55,7,98,43,3,0,17,9,8,]
for n in num:
    
    if n % 2 == 0:
        print(n,"número par")
        if n == 0:
         print("El número es cero")
    elif n % 2 == 1:
        print(n,"número impar")
    else:
        print()
