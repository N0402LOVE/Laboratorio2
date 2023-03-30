print("PROGRAMA QUE SOLICITA 3 NÚMEROS ENTEROS ")

número1=int(input("Ingrese el primer número:"))

número2=int(input("Ingrese el segundo número:"))

número3=int(input("Ingrese el tercer  número:"))

if número1 > número2 :
    print (int("El número "),número1 ("es el número más grande de los 3"))
    
    if número1 < número2 and  número2 < número3: 
        
       print (int("El número "),número2 ("es el más pequeño de los 3"))
       
    elif número1 > número2 and número2 < número3:
     print (int("El número"),número3 ("es el número de en medio de los 3"))
else:
    print("FIN DEL PROGRAMA")
    
 
   