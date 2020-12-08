# Codigo basado en el proyecto elaborado por el Ingeniero Luis Espino, bajo la licencia MIT
# Luis Espino 2020
import os
import subprocess
import time

class Node:
    def __init__(self, value):
        self.value  = value
        self.left   = None
        self.right  = None
        self.height = 0

class AVLTree:
    def __init__(self):
        self.root = None

    #add
        
    def add(self, value):
        self.root = self._add(value, self.root)
    
    def _add(self, value, tmp):
        if tmp is None:
            return Node(value)        
        elif value>tmp.value:
            tmp.right=self._add(value, tmp.right)
            if (self.height(tmp.right)-self.height(tmp.left))==2:
                if value>tmp.right.value:
                    tmp = self.srr(tmp)
                else:
                    tmp = self.drr(tmp)
        else:
            tmp.left=self._add(value, tmp.left)
            if (self.height(tmp.left)-self.height(tmp.right))==2:
                if value<tmp.left.value:
                    tmp = self.srl(tmp)
                else:
                    tmp = self.drl(tmp)
        r = self.height(tmp.right)
        l = self.height(tmp.left)
        m = self.maxi(r, l)
        tmp.height = m+1
        return tmp

    def height(self, tmp):
        if tmp is None:
            return -1
        else:
            return tmp.height
        
    def maxi(self, r, l):
        return (l,r)[r>l]   

    #rotations

    def srl(self, t1):
        t2 = t1.left
        t1.left = t2.right
        t2.right = t1
        t1.height = self.maxi(self.height(t1.left), self.height(t1.right))+1
        t2.height = self.maxi(self.height(t2.left), t1.height)+1
        return t2

    def srr(self, t1):
        t2 = t1.right
        t1.right = t2.left
        t2.left = t1
        t1.height = self.maxi(self.height(t1.left), self.height(t1.right))+1
        t2.height = self.maxi(self.height(t2.left), t1.height)+1
        return t2
    
    def drl(self, tmp):
        tmp.left = self.srr(tmp.left)
        return self.srl(tmp)
    
    def drr(self, tmp):
        tmp.right = self.srl(tmp.right)
        return self.srr(tmp)

    #traversals

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, tmp):
        if tmp:
            print(tmp.value,end = ' ')
            self._preorder(tmp.left)            
            self._preorder(tmp.right)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, tmp):
        if tmp:
            self._inorder(tmp.left)
            print(str(tmp.value) + ', '+ str(tmp.height),end = ' ')
            self._inorder(tmp.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, tmp):
        if tmp:
            self._postorder(tmp.left)            
            self._postorder(tmp.right)
            print(tmp.value,end = ' ')

    def DefinirNodos(self, tmp, file):
        if tmp:
            if tmp.left:
                file.write(str(tmp.value) + '->' + str(tmp.left.value) + os.linesep)
            if tmp.right:
                file.write(str(tmp.value) + '->' + str(tmp.right.value) + os.linesep)
            self.DefinirNodos(tmp.left, file)            
            self.DefinirNodos(tmp.right, file)

    def ImprimirArbol(self):
        self._ImprimirArbol(self.root)

    def _ImprimirArbol(self, tmp):
        file = open('arbol.dot', "w")
        file.write("digraph grafica{" + os.linesep)
        file.write("rankdir=TB;" + os.linesep)
        file.write("node [shape = circle];" + os.linesep)
        self.DefinirNodos(self.root, file)
        file.write("}" + os.linesep)
        file.close()
        subprocess.call('dot -Tpng arbol.dot -o arbol.png')
        os.system('arbol.png')

    def buscar(self, valor):
        return self._buscar(self.root, valor)

    def _buscar(self, tmp, valor):
        if tmp:
            if tmp.value == valor:
                return tmp
            elif tmp.value > valor:
                return self._buscar(tmp.left, valor)
            else:
                return self._buscar(tmp.right, valor)
        else:
            raise ValueError('El numero no esta en el arbol')
        
    def Eliminar(self, valor):
        self._Eliminar(self.root, valor)

    def _Eliminar(self, tmp, valor):
        padre = None
        lado = None
        while tmp != None:
            if tmp.value == valor:
                if padre == None:
                    if tmp.left == None and tmp.right != None:
                        tmp.value = tmp.right.value
                        tmp.right = None 
                        tmp.height = 0
                    else:
                        recorrido = tmp.left
                        if recorrido.right == None and recorrido.left == None:
                            tmp.value = recorrido.value
                            tmp.left = None
                            recorrido = None
                            tmp.height = 0
                        else:
                            hijo = 1
                            while hijo != None:
                                padre = recorrido 
                                recorrido = recorrido.right
                                hijo = recorrido.right
                            if recorrido.left == None:
                                tmp.value = recorrido.value
                                padre.right = None
                                if padre.left == None:
                                    padre.height = 0
                            else:
                                tmp.value = recorrido.value
                                recorrido.value = recorrido.left.value
                                recorrido.left = None
                                recorrido.height = 0
                    if padre.right == None and padre.left == None:
                        padre.height =- 1
                    
                else:
                    if lado == 'i':
                        if tmp.right == None and tmp.left == None:
                            padre.left = None
                            tmp = None
                        elif tmp.left == None and tmp.right != None:
                            tmp.value = tmp.right.value
                            tmp.right = None
                            tmp.height = 0
                        else:
                            recorrido = tmp.left
                            if recorrido.right == None and recorrido.left == None:
                                tmp.value = recorrido.value
                                tmp.left = None
                                recorrido = None
                                tmp.height = 0
                            else:
                                hijo = 1
                                while hijo != None:
                                    padre = recorrido 
                                    recorrido = recorrido.right
                                    hijo = recorrido.right
                                if recorrido.left == None:
                                    tmp.value = recorrido.value
                                    padre.right = None
                                    if padre.left == None:
                                        padre.height = 0
                                else:
                                    tmp.value = recorrido.value
                                    recorrido.value = recorrido.left.value
                                    recorrido.left = None
                                    recorrido.height = 0
                        if padre.right == None and padre.left == None:
                            padre.height =- 1
                        
                    else:
                        if tmp.right == None and tmp.left == None:
                            padre.right = None
                            tmp = None
                        elif tmp.left == None and tmp.right != None:
                            tmp.value = tmp.right.value
                            tmp.right = None
                            tmp.height = 0
                        else:
                            recorrido = tmp.left
                            if recorrido.right == None and recorrido.left == None:
                                tmp.value = recorrido.value
                                tmp.left = None
                                recorrido = None
                                tmp.height = 0
                            else:
                                hijo = 1
                                while hijo != None:
                                    padre = recorrido 
                                    recorrido = recorrido.right
                                    hijo = recorrido.right
                                if recorrido.left == None:
                                    tmp.value = recorrido.value
                                    padre.right = None
                                    if padre.left == None:
                                        padre.height = 0
                                else:
                                    tmp.value = recorrido.value
                                    recorrido.value = recorrido.left.value
                                    recorrido.left = None
                                    recorrido.height = 0
                        if padre.right == None and padre.left == None:
                            padre.height =- 1
            elif tmp.value > valor:
                padre = tmp
                tmp = tmp.left
                lado = 'i'
            else:
                padre = tmp
                tmp = tmp.right
                lado = 'd'







           

#init
t = AVLTree()

#add
t.add(5)
t.add(10)
t.add(20)
t.add(25)
t.add(30)
t.add(35)
t.add(50)
t.add(6)
t.add(11)
t.add(21)
t.add(26)
t.add(31)
t.add(36)
t.add(51)

#print traversals
t.preorder()
print()
t.inorder()
print()
t.postorder()
print()
print(str(t.buscar(10).value))


t.ImprimirArbol()
time.sleep(5)
t.Eliminar(25)
t.ImprimirArbol()
print()
t.inorder()
print()