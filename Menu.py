from ListaEnlazadaOrden import ListaEnlazadaOrden, Orden
from ListaEnlazadaPizza import Pizza
from ListaEnlazadaIngrediente import Ingrediente

class Menu:
    def __init__(self):
        
        opcion = 0
        self.lista_orden = ListaEnlazadaOrden()

        while opcion != 5:
            print("\nMenu Principal: \n1.Ingresar Orden \n2.Mostrar Lista de Ordenes \n3.Mostrar Graficamente La Orden" 
            "\n4.Seleccionar una Orden" 
            "\n5.Salida")
            
            opcion = int(input("Ingrese una opcion \n"))
            
            if opcion == 1:
                nombre_cliente = str(input("Ingrese el nombre del cliente: "))
                cantidad_pizzas = int(input("Ingrese la cantidad de pizzas: ")) 

                
                self.lista_orden.append(Orden(nombre_cliente, cantidad_pizzas))


                for i in range(cantidad_pizzas):
                    self.lista_orden.findByNombreCliente(nombre_cliente).lista_pizzas.append(Pizza(i+1))
                    opc = 0
                    while opc != 2:
                        print("\n1.Ingresar ingrediente de pizza ",i+1,"\n2.Salir")                
                        opc = int(input("Ingrese la opcion: "))

                        if opc == 1:                       
                            ingrediente = input("Ingrese el ingrediente de pizza: ")
                            self.lista_orden.findByNombreCliente(nombre_cliente).lista_pizzas.findByPizza(i+1).lista_ingredientes.append(Ingrediente(ingrediente))
                        elif opc == 2:
                            print("SALIO\n")
                        else:
                            print("Ingrese una opcion correcta")
                
                self.lista_orden.findByNombreCliente("Fernando").lista_pizzas.findByPizza(1).lista_ingredientes.printListaEnlazadaIngrediente()
                
            elif opcion == 2:
                self.lista_orden.printListaEnlazadaOrden()
                self.lista_orden.findByNombreCliente("Fernando").lista_pizzas.findByPizza(1).lista_ingredientes.printListaEnlazadaIngrediente()                    
            elif opcion == 3:

                print("Mostrar Graficamente la Orden")

            elif opcion == 4:
                pass
                
            elif opcion == 5:
                print("salio")  
                
            else:
                print("\nIngresa una opcion correcta \n") 


obj = Menu()
