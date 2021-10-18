# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 18:33:35 2021

@author: itzam
"""
import numpy as np

class tableau:
    
    def __init__(self,A,b,c):
        
        #Número de restricciones
        self.p = np.shape(A)[0]
        #Número de variables    
        self.n = np.shape(A)[1]
        
        
        
        #Matriz extendida para variables de holgura
        #Añadimos una por restricción
        self.A = np.zeros((self.p,self.n+self.p))
        
        self.A[:,:self.n]=A
        self.A[:,self.n:]=np.eye(self.p)
        
        #Ahora transformamos el vector de costos
        #(c1,c2,...,cn) a (c1,c2,...,cn,0,0,,,,,0)
        #Es un vector columna
        self.c = np.zeros((self.p+self.n,1))
        c = c.reshape(self.n,1)
        self.c[:self.n]=c
        
        self.b = b.reshape(self.p,1)
        
        
        #Para identificar a la base, usaremos un vector 
        #de dimensión p (número de restricciones), donde 
        #guardaremos los índices de las variables que en
        #ese momento se encuentran en la base, por ejemplo:
            
        #base = [5,0,1] significa que las variables en la base son 5,0,1
        #Al inicio las variables en la base son las de holgura
        
        self.base = np.arange(self.n,self.n+self.p)
        
        #las variables no básicas siempre irán de menor a mayor
        self.nobase = np.delete(np.arange(0,self.n+self.p),self.base)
        #Aqui tomamos un rango 0,1,...,n+p y posteriormente retiramos las 
        #posiciones correspondientes a las variables en la base, por ejemplo
        
        #0,1,2,3,4,5,6 y en la base están [5,0,1]
        #Eliminamos entonces las posiciones 5,0,1 que corresponden con indices
        #5,0,1, resultando : 2,3,4,6
        
        #Solución provisional
        self.solucion = np.zeros(self.n+self.p)
        
        #Ahorros provisionales
        self.ahorros = np.zeros(self.n+self.p)
        
    def Simplex(self):  
        
        #Contador de iteraciones
        itera = 0
        
        while(True):
            
            #Selecciono de la mátriz A, las columnas correspondientes 
            #las variables básicas
            A_b = self.A[:,self.base]
            A_n = self.A[:,self.nobase]
            #Selecciono del coeficiente de costos, aquellos correspondientes
            #a las variables básicas
            c_b = self.c[self.base]
            c_n = self.c[self.nobase]
            
            lambda_simplex = np.linalg.solve(A_b.T,c_b) #El resultado
            #sí es un vector columna (comprobado)
            
            #ahorros_nb actualmente está en vector renglón.
            ahorros_nb = lambda_simplex.T@A_n-c_n.T
            
            if((ahorros_nb<=0).all()):
                #Terminamos y regresamos la solucion
                
                z_0 = lambda_simplex.T@self.b
                self.solucion[self.base]=(np.linalg.inv(A_b)@self.b).reshape(
                    1,self.p)
                return (self.solucion[:self.n],z_0,0,itera)
                
            #PREGUNTAAA
            #Dijo que sí
            self.ahorros[self.base]=0
            #Si existe un ahorro positivo, esa es la variable que debe entrar
            self.ahorros[self.nobase]=ahorros_nb
            #¿Hay que actualizar los ahorros de la base? ¿Hacerlos cero?
            #Lo hago como prueba
            
            
            #Ahora obtenemos el índice de la primer variable que tiene ahorro
            #positivo
            
            e = np.where(self.ahorros>0)[0][0]
            
            
            #Ahora determinemos si existe variable de salida y , si existe, 
            #determinar la variable de salida
            
            #H_e en vector columna
            H_e = np.linalg.solve(A_b,self.A[:,e].reshape(self.p,1))
            
            #Ahora, vemos si el problema es no acotado
            if((H_e<=0).all()):
                #El problema es no acotado y terminamos
                return (self.solucion[self.base],0,1,itera)
            
            #h también está en vector columna
            h = np.linalg.solve(A_b, self.b)
            
            #Ahora hay que determinar la variable de salida
            #queremos tomar el minimo solo de los valores positivos
            
            #Primero eliminamos las posibilidades de que H_e se anule y la
            #división no se pueda realizar: cambiamos 0 por una entrada negativa
            H_e_temp = np.where(H_e==0,-1,H_e)
            
            #Ahora atendemos donde se haga negativa
            #Donde haya una entrada negativa en H_e, haremos la correspondiente
            #entrada de h -inf y así h/H_e dara inf en esa entrada
            
            h_temp = np.where(H_e<=0,-np.inf,h)
            
            #Ahora debemos encontrar la posición dentro de la base tal 
            #que el cociente es minimo
            s_tilde = np.argmin(h_temp/H_e_temp)
            #Esta es la posición dentro de la base, no el indice de la variable
            #Ejemplo: [5,0,1]
            #y tenemos que s_tilde = 0, entonces debe salir x_5
            #El indice de la variable que sale es base[s_tilde]
            
            #entra e 
            self.base[s_tilde]=e
            
            #Actualizamos las no bases
            self.nobase = np.delete(np.arange(0,self.n+self.p),self.base)
            itera+=1
            
      
def mSimplexFaseII(A,b,c):
    tabla = tableau(A,b,c)
    solucion = tabla.Simplex()
    return solucion
        
# Ejemplo 1
# A = np.array([[ 1,  1,  2],
#         [ 1,  1, -1],
#         [-1,  1,  1]])

# b = np.array([[9],
#         [2],
#         [4]])

# c = np.array([[ 1],
#         [ 1],
#         [-4]])

# tabla1 = tableau(A,b,c)
# answ = tabla1.Simplex()
# print(answ[0])
            

#Ejemplo 2

# A = np.array([
#     [1,-1],
#     [1,1]
#     ])
# b = np.array([[2],[6]])
# c = np.array([[1],[-1]])
# tabla1 = tableau(A,b,c)
# answ = tabla1.Simplex()
# print(answ[0])      

#Ejemplo 3

# A = np.array([
#     [-1,1],
#     [1,0]
#     ])
# b = np.array([[0],[2]])
# c = np.array([[0],[-1]])
# tabla1 = tableau(A,b,c)
# answ = tabla1.Simplex()
# print(answ[0])          
                
            
            
            
        
        
        