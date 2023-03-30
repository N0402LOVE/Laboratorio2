print("Programa para determinar el cambio ")
print("")
producto=input("Ingrese el nombre del producto :").lower()
precio=int (input("Ingrese el precio del producto :"))
pago=int(input("Ingrese su pago para determinar el cambio :" ))
print("")
if pago > precio :
    cambio= pago-precio
    print("SU CAMBIO ES DE : $",cambio)
elif pago==precio:
    print("NO SE LE ENTREGARÁ CAMBIO")   
elif pago < precio:
    cambIo= precio-pago
    print("El dinero faltante para completar el pago es : $" ,cambIo) 
else:
    print(" Error")    