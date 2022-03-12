from ListaEnlazadaIngrediente import ListaEnlazadaIngrediente

class Pizza:
    def __init__(self, pizza = None):
        self.pizza = pizza
        self.siguiente = None
        self.lista_ingredientes = ListaEnlazadaIngrediente()

class ListaEnlazadaPizza:
    def __init__(self):
        self.raiz = Pizza()
        self.ultimo = Pizza()
        
    
    def append(self, nuevoNodo):
        if self.raiz.pizza is None:
            self.raiz = nuevoNodo
            self.ultimo = nuevoNodo
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            self.ultimo.siguiente = nuevoNodo
            self.ultimo = nuevoNodo

    def pop(self, pizza = None):
        if pizza is None:
            if self.raiz.siguiente is None:
                self.raiz = Pizza()
            else:
                nodoaux = self.raiz
                nodoPenultimo = nodoaux
                
                while nodoaux.siguiente is not None:
                    nodoPenultimo = nodoaux
                    nodoaux = nodoaux.siguiente
                
                nodoPenultimo.siguiente = None
        else:
            if self.raiz.pizza == pizza:
                if self.raiz.siguiente is not None:
                    self.raiz = self.raiz.siguiente
                else:
                    self.raiz = Pizza()
            else:
                nodoaux = self.raiz
                nodoAnterior = nodoaux
                
                while nodoaux.pizza != pizza:
                    nodoAnterior = nodoaux
                    nodoaux = nodoaux.siguiente
                    
                nodoAnterior.siguiente = nodoaux.siguiente
                    
    def findByPizza(self, pizza):
        nodoaux = self.raiz
        
        while nodoaux.pizza != pizza:
            if nodoaux.siguiente is not None:
                nodoaux = nodoaux.siguiente
            else:
                return None
        return nodoaux
                  
                
    
    def printListaEnlazadaPizza(self):
        nodoAux = self.raiz
        
        cadena = ''
        while True:
            if nodoAux.pizza is not None:
                cadena += '(' + str(nodoAux.pizza) + ') -> '
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                else:
                    break
            else:
                break
        print(cadena)