from ListaEnlazadaOrden import ListaEnlazadaOrden, Orden
from ListaEnlazadaPizza import Pizza
from ListaEnlazadaIngrediente import Ingrediente
import time
from datetime import datetime

class Menu:
    def __init__(self):
        
        opcion = 0
        self.lista_orden = ListaEnlazadaOrden()
        self.tiempo_espera = 0

        while opcion != 5:
            print("\nMenu Principal: \n1.Ingresar Orden \n2.Mostrar Lista de Ordenes \n3.Entregar Orden" 
            "\n4.Mostrar Datos del Desarrollador" 
            "\n5.Salida")
            
            opcion = int(input("Ingrese una opcion \n"))
            
            if opcion == 1:
                nombre_cliente = str(input("Ingrese el nombre del cliente: "))
                cantidad_pizzas = int(input("Ingrese la cantidad de pizzas: ")) 

                now = datetime.now()
                hora = now.hour
                minuto = now.minute
                segundo = now.second
                hora_inicio = str(hora)+":"+ str(minuto)+":"+str(segundo)
                self.lista_orden.append(Orden(nombre_cliente, cantidad_pizzas, hora_inicio))
                self.tiempo_espera = self.tiempo_espera + now.minute
                pepperoni = 3
                salchicha = 4
                carne = 10
                queso = 5
                pina = 2

                self.contador_tiempo= 0
                for i in range(cantidad_pizzas):
                    self.lista_orden.findByNombreCliente(nombre_cliente).lista_pizzas.append(Pizza(i+1))
                    opc = 0
                    while opc != 2:
                        print("\n1.Ingresar ingrediente de pizza ",i+1,"\n2.Salir")                
                        opc = int(input("Ingrese la opcion: "))

                        if opc == 1:                       
                            ingrediente = str(input("Ingrese el ingrediente de pizza: "))
                            if ingrediente == 'pepperoni':
                                self.lista_orden.findByNombreCliente(nombre_cliente).lista_pizzas.findByPizza(i+1).lista_ingredientes.append(Ingrediente(ingrediente, pepperoni))
                                self.contador_tiempo = self.contador_tiempo+pepperoni
                            elif ingrediente == 'salchicha':
                                self.lista_orden.findByNombreCliente(nombre_cliente).lista_pizzas.findByPizza(i+1).lista_ingredientes.append(Ingrediente(ingrediente, salchicha))
                                self.contador_tiempo = self.contador_tiempo+salchicha
                            elif ingrediente == 'carne':
                                self.lista_orden.findByNombreCliente(nombre_cliente).lista_pizzas.findByPizza(i+1).lista_ingredientes.append(Ingrediente(ingrediente, carne))
                                self.contador_tiempo = self.contador_tiempo+carne
                            elif ingrediente == 'queso':
                                self.lista_orden.findByNombreCliente(nombre_cliente).lista_pizzas.findByPizza(i+1).lista_ingredientes.append(Ingrediente(ingrediente, queso))
                                self.contador_tiempo = self.contador_tiempo+queso
                            elif ingrediente == 'pina':
                                self.lista_orden.findByNombreCliente(nombre_cliente).lista_pizzas.findByPizza(i+1).lista_ingredientes.append(Ingrediente(ingrediente, pina))
                                self.contador_tiempo = self.contador_tiempo+pina
                        elif opc == 2:
                            print("SALIO\n")
                        else:
                            print("Ingrese una opcion correcta")
                    
                    print("El tiempo total en hacer la pizza ",i+1, " es: ",self.contador_tiempo)
                    self.tiempo_espera = self.tiempo_espera+self.contador_tiempo
                    #self.lista_orden.findByNombreCliente(nombre_cliente).lista_pizzas.findByPizza(i+1).lista_ingredientes.printListaEnlazadaIngrediente()
                print("tiempo en espera: ", self.tiempo_espera)  
                hora_final = str(hora)+":"+str(self.tiempo_espera)+":"+str(segundo) 
                self.lista_orden.findByNombreCliente(nombre_cliente).horaFinal(hora_final)

            elif opcion == 2:
                self.lista_orden.printListaEnlazadaIngresarOrden()
                #self.lista_orden.findByNombreCliente("Fernando").lista_pizzas.findByPizza(1).lista_ingredientes.printListaEnlazadaIngrediente()                    
            elif opcion == 3:
                print("Entregando orden.......")
                entregado = self.lista_orden.pop()
                print("cliente: ",entregado.nombre_cliente," hora de entrega: ",entregado.hora_final)
                self.lista_orden.printListaEnlazadaEntregarOrden()

            elif opcion == 4:
                print("Nombre: Luis Fernando Gonzalez Real\n","Carrera: Ingenieria en Ciencias y Sistemas\n" ,"Carne: 201313965")
                hora_actual = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                
                now = datetime.now()
                print("hora: ", now.hour," minutos: ",now.minute, " segundos: ", now.second)
                
            elif opcion == 5:
                print("salio")  
                
            else:
                print("\nIngresa una opcion correcta \n") 


obj = Menu()
