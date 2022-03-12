from ListaEnlazadaPizza import ListaEnlazadaPizza

class Orden:
    def __init__(self, nombre_cliente = None, cantidad_pizzas= None):
        self.nombre_cliente = nombre_cliente
        self.cantidad_pizzas = cantidad_pizzas
        self.siguiente = None
        self.lista_pizzas = ListaEnlazadaPizza()

class ListaEnlazadaOrden:
    def __init__(self):
        self.raiz = Orden()
        self.ultimo = Orden()
        
    
    def append(self, nuevoNodo):
        if self.raiz.nombre_cliente is None:
            self.raiz = nuevoNodo
            self.ultimo = nuevoNodo
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            self.ultimo.siguiente = nuevoNodo
            self.ultimo = nuevoNodo

    def pop(self, nombre_cliente = None):
        if nombre_cliente is None:
            if self.raiz.siguiente is None:
                self.raiz = Orden()
            else:
                nodoaux = self.raiz
                nodoPenultimo = nodoaux
                
                while nodoaux.siguiente is not None:
                    nodoPenultimo = nodoaux
                    nodoaux = nodoaux.siguiente
                
                nodoPenultimo.siguiente = None
        else:
            if self.raiz.nombre_cliente == nombre_cliente:
                if self.raiz.siguiente is not None:
                    self.raiz = self.raiz.siguiente
                else:
                    self.raiz = Orden()
            else:
                nodoaux = self.raiz
                nodoAnterior = nodoaux
                
                while nodoaux.nombre_cliente != nombre_cliente:
                    nodoAnterior = nodoaux
                    nodoaux = nodoaux.siguiente
                    
                nodoAnterior.siguiente = nodoaux.siguiente
                    
    def findByNombreCliente(self, nombre_cliente):
        nodoaux = self.raiz
        
        while nodoaux.nombre_cliente != nombre_cliente:
            if nodoaux.siguiente is not None:
                nodoaux = nodoaux.siguiente
            else:
                return None
        return nodoaux
                  
                
    
    def printListaEnlazadaOrden(self):
        nodoAux = self.raiz
        
        cadena = ''
        while True:
            if nodoAux.nombre_cliente is not None:
                cadena += '(' + nodoAux.nombre_cliente + '-' + str(nodoAux.cantidad_pizzas) + ') -> '
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                else:
                    break
            else:
                break
        print(cadena)