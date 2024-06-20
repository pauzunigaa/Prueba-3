sectores=[]
def registrar_pedido(pedidos):
    while True:# validando nombre
        nombreyApellido=input(" Ingrese Nombre y Apellido: ")
        if nombreyApellido=="":
            print(" Ingrese Nombre y Apellido")
        else:
            print()
        break

    while True:# validando direccion
        direccion=input("Ingrese direccion: ")
        break

    while True: #validando sector
        try:
            sector=input("Ingrese sector (centro / norte / sur ):").lower()
            if sector=="":
                print("Ingrese sector (centro / norte / sur ")
            else:
                break
        except ValueError:
            print("Ingrese solo una de las opciones indicada")
        

    contadorpeq=0
    contadorMed=0
    contadorGran=0
    while True:
        try:
            print(" ********** Detalle del pedido **********")
            print("1.- Pequeño")
            print("2.- Mediano")
            print("3.-Grande")
            print("4.-Salir")
            
            opcionpaq=int(input(" Seleccione el tamaño del paquete : "))
            
            if opcionpaq!=4:
                cantpaq=int(input(" Ingrese cantidad de paquetes"))


            if opcionpaq==1:
                contadorpeq=contadorpeq+cantpaq
            elif opcionpaq==2:
                contadorMed=contadorMed+cantpaq
            elif opcionpaq==3:
                contadorpeq=contadorGran+cantpaq
            elif opcionpaq==4:
                break
            else:
                print(" Ingrese una opciuon valida")
        except ValueError:
            print(" Ingrese una opcion valida")
       

    pedido={
        "Nombre y Apellido":nombreyApellido,
        "Direccion":direccion,
        "Sector":sector,
        "Pequeño":contadorpeq,
        "Mediano":contadorMed,
        "Grande":contadorGran,
        
    }
    pedidos.append(pedido)


def listar_pedidos(pedidos):
    for pedido in pedidos:
        print("Nombre y Apellido",pedido["Nombre y Apellido"])
        print("Direccion",pedido["Direccion"])
        print("Sector",pedido["Sector"])
        print("Pequeño",pedido["Pequeño"])
        print("Mediano",pedido["Mediano"])
        print("Grande",pedido["Grande"])



        
def imprimir_hojaRuta(pedidos):

    with open("hoja_ruta.txt","w") as archivo:
        for pedido in pedidos:
            archivo.write(pedido["Nombre y Apellido"])
            archivo.write("\n")
            archivo.write(pedido["Direccion"])
            archivo.write("\n")     
            archivo.write(pedido["Sector"])
            archivo.write("\n")
            archivo.write(f"{pedido["Pequeño"]}")
            archivo.write("\n")
            archivo.write(f"{pedido["Mediano"]}")
            archivo.write("\n")
            archivo.write(f"{pedido["Grande"]}")
            archivo.write("\n")



