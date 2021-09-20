#Ejercicios Taller Ciclos - Carlos Ayala
from numpy.random import randint
import numpy as np
import random
from statistics import mean

# Ejercicio 1
def num1():
  n = int(input("digite la cantidad de autos\n"))
  i = 1
  amarillo = 0
  rosa = 0
  rojo = 0
  verde = 0
  azul = 0
  print("***Digito del automovil***")
  print("1 o 2 amarillo")
  print("3 o 4 rosa")
  print("5 o 6 rojo")
  print("7 o 8 verde")
  print("9 o 0 azul")
  while i <= n:
      digito = int(input("escriba el ultimo digito de la placa de su auto\n"))
      if(digito == 1 ) | (digito == 2):
          amarillo = amarillo + 1
      elif(digito == 3) | (digito == 4):
          rosa = rosa + 1
      elif(digito == 5) | (digito == 6):
          rojo = rojo + 1
      elif(digito == 7) | (digito == 8):
              verde = verde + 1
      elif(digito == 9) | (digito == 0):
              azul = azul + 1
      i+=1
  print("total de automoviles con calcomania amarillo", amarillo)
  print("total de automoviles con calcomania rosa", rosa)
  print("total de automoviles con calcomania rojo", rojo)
  print("total de automoviles con calcomania verde", verde)
  print("total de automoviles con calcomania azul", azul)
  print("######################################################") 
