
pedidos=[]
import funciones as fn
while True:
        try:
            print(" ********** PaquExpress **********")
            print()
            print("1. Registrar pedido")
            print("2 Listar todos los pedidos")
            print("3. Imprimir hoja de ruta")
            print("4. Salir del programa")

            opcionMenu=int(input("Ingrese una opcion :"))

            if opcionMenu==1:
                    fn.registrar_pedido(pedidos)
            elif opcionMenu==2:
                    fn.listar_pedidos(pedidos)
            elif opcionMenu==3:
                    fn.imprimir_hojaRuta(pedidos)
            elif opcionMenu==4:
                    print(" Saliendo del programa...")
                    break
            else:
                print(" Ingrese una opcion valida")
        except ValueError:
            print("Ingrese una opcion valida entre 1 y 4")