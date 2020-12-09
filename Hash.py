class Nodo:
    def __init__(self, indice, clave, valor):
        self.indice = indice
        self.clave = clave
        self.valor = valor

class Hash:
    def __init__(self, valor=7):
        self.vector = []
        self.elementos = 0
        self.factorCarga = 0
        self.tamaño = valor

        for i in range(valor):
            self.vector.append(None)

    def print(self):
        contador = 0
        for i in self.vector:
            if i:
                print("Indice:", contador, "Valor:", i.valor)
            else:
                print("Indice:", contador, "Valor:", i)
            contador += 1

    def insertar(self, id, clave, valor):
        posicion = self.funcion_hash(id)
        nuevo = Nodo(posicion, clave, valor)
        self.vector[posicion] = nuevo
        self.elementos += 1
        self.factorCarga = self.elementos/self.tamaño

        if self.factorCarga > 0.8:
            self.rehashing()
    
    def rehashing(self):
        siguiente = self.tamaño
        factor = 0
        while(factor < 0.3):
            siguiente += 1
            factor = self.elementos/siguiente
        temporal = []
        for i in range(siguiente):
            temporal.append(None)

        contador = 0
        for i in self.vector:
            temporal[contador] = i
            contador += 1
        
        self.vector = temporal
        self.tamaño = siguiente

    def funcion_hash(self, id):
    
        posicion = id % self.tamaño
        while(self.vector[posicion] != None):
            posicion += 1
            if posicion > self.tamaño:
                posicion = posicion - self.tamaño
        return posicion 

    def toASCII(self, cadena):
        result = 0
        for char in cadena:
            result += ord(char)
        return result