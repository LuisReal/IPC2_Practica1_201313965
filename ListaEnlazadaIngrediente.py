
class Ingrediente:
    def __init__(self,  ingrediente = None, tiempo = None):
        self.ingrediente = ingrediente
        self.tiempo = tiempo
        self.siguiente = None
        

class ListaEnlazadaIngrediente:
    def __init__(self):
        self.raiz = Ingrediente()
        self.ultimo = Ingrediente()
        
    
    def append(self, nuevoNodo):
        if self.raiz.ingrediente is None:
            self.raiz = nuevoNodo
            self.ultimo = nuevoNodo
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            self.ultimo.siguiente = nuevoNodo
            self.ultimo = nuevoNodo

    def pop(self, ingrediente = None):
        if ingrediente is None:
            if self.raiz.siguiente is None:
                self.raiz = Ingrediente()
            else:
                nodoaux = self.raiz
                nodoPenultimo = nodoaux
                
                while nodoaux.siguiente is not None:
                    nodoPenultimo = nodoaux
                    nodoaux = nodoaux.siguiente
                
                nodoPenultimo.siguiente = None
        else:
            if self.raiz.ingrediente == ingrediente:
                if self.raiz.siguiente is not None:
                    self.raiz = self.raiz.siguiente
                else:
                    self.raiz = Ingrediente()
            else:
                nodoaux = self.raiz
                nodoAnterior = nodoaux
                
                while nodoaux.ingrediente != ingrediente:
                    nodoAnterior = nodoaux
                    nodoaux = nodoaux.siguiente
                    
                nodoAnterior.siguiente = nodoaux.siguiente
                    
    def findByIngrediente(self, ingrediente):
        nodoaux = self.raiz
        
        while nodoaux.ingrediente != ingrediente:
            if nodoaux.siguiente is not None:
                nodoaux = nodoaux.siguiente
            else:
                return None
        return nodoaux
                  
                
    
    def printListaEnlazadaIngrediente(self):
        nodoAux = self.raiz
        
        cadena = ''
        while True:
            if nodoAux.ingrediente is not None:
                cadena += '(' +" ingrediente: "+ nodoAux.ingrediente +" tiempo:"+ str(nodoAux.tiempo)+') -> '
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                else:
                    break
            else:
                break
        print(cadena)