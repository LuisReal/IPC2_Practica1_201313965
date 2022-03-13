from ListaEnlazadaPizza import ListaEnlazadaPizza

class Orden:
    def __init__(self, nombre_cliente = None, cantidad_pizzas= None, hora_inicio = None, hora_final = None):
        self.nombre_cliente = nombre_cliente
        self.cantidad_pizzas = cantidad_pizzas
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final
        self.siguiente = None
        self.anterior = None
        self.lista_pizzas = ListaEnlazadaPizza()
    
    def horaFinal(self, hora):
        self.hora_final = hora

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
            self.ultimo.anterior = self.raiz
        else:
            self.ultimo.siguiente = nuevoNodo
            nuevoNodo.anterior = self.ultimo
            self.ultimo = nuevoNodo
    
    def insertar(self, nuevo):
        if self.ultimo.nombre_cliente is None:
            self.raiz = nuevo
            self.ultimo = nuevo
        else:
            pass

    def pop(self, nombre_cliente = None):
        if nombre_cliente is None:
            if self.ultimo.anterior is None:
                self.ultimo = Orden()
                return self.ultimo
            else:
                nodoaux = self.ultimo
                nodoPenultimo = nodoaux
                
                while nodoaux.anterior is not None:
                    nodoPenultimo = nodoaux
                    nodoaux = nodoaux.anterior
                
                nodoPenultimo.anterior = None
                return nodoaux
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
                  
                
    
    def printListaEnlazadaIngresarOrden(self):
        nodoAux = self.ultimo
        
        cadena = ''
        while True:
            if nodoAux.nombre_cliente is not None:
                cadena += '(' + nodoAux.nombre_cliente + '-' + str(nodoAux.cantidad_pizzas) + '-'+ nodoAux.hora_inicio+') -> '
                if nodoAux.anterior is not None:
                    nodoAux = nodoAux.anterior
                else:
                    break
            else:
                break
        print(cadena)
    
    def printListaEnlazadaEntregarOrden(self):
        nodoAux = self.ultimo
        
        cadena = ''
        while True:
            if nodoAux.nombre_cliente is not None:
                cadena += '(' + nodoAux.nombre_cliente + '-' + str(nodoAux.cantidad_pizzas) + '-'+ nodoAux.hora_final+') -> '
                if nodoAux.anterior is not None:
                    nodoAux = nodoAux.anterior
                else:
                    break
            else:
                break
        print(cadena)