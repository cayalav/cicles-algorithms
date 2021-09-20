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

# Ejercicio 2
def num2():
  print('¿Digite un numero del animal que estudiara? 1. Elefante, 2. Jirafas, 3. Chimpancés:')
  inp = int(input())
  if inp == 1: cicle = 20
  if inp == 2: cicle = 15
  if inp == 3: cicle = 40
  values = randint(0, 6, cicle)
  count_arr = np.bincount(values)
  count_arr = np.bincount(values)
  cat1 = (count_arr[0] + count_arr[1])*100/cicle
  cat2 = count_arr[2]*100/cicle
  cat3 = (count_arr[3] + count_arr[4] + count_arr[5])*100/cicle
  print(f"muestra de "+str(cicle)+" numeros")
  print(f""+str(cat1)+"%"+" de las edades son de 0 a 1 año")
  print(f""+str(cat2)+"%"+" de las edades son de mas de 1 año y menos de 3 años")
  print(f""+str(cat3)+"%"+" de las edades son de mas de 3 años")

  print("######################################################")  

# Ejercicio 3
def num3():
  t = int(input("Escribe el numero de trabajadores\n"))
  x = 1
  salario = 0
  horas_extra = 0
  while x <= t:
    h = int(input("escribe el numero de horas trabajadas\n"))
     
    if(h <= 40):
        salario = h * 20
        print("el salario del trabajador ",x," es:", salario)
    else:
      horas_extra = h - 40
      salario = (40 * 20) + (horas_extra * 25)
      print("el salario del trabajador ",x," es:", salario)
    x+=1     
  print("######################################################")  

# Ejercicio 4
def num4():
  StudentGrades = {
    'Hombres': [15, 17],
    'Mujeres': [23, 19]
    } 
  avgDict = {}
  suma=0
  lend=0
  for k,v in StudentGrades.items():
    avgDict[k] = sum(v)/ float(len(v))
    suma=suma+sum(v)
    lend=lend+len(v)
  print(avgDict)
  print(f"Promedio total = "+str(suma/lend))
  print("######################################################") 

# Ejercicio 5
def num5():
  n = int(input("escribe el total de numeros a calcular\n"))
  x = 1
  while(x <= n):
    numero = int(input("escriba un numero\n"))
    if(x == 1):
        menor = numero
    else:
        if(numero < menor):
            menor = numero
    x+=1
  print("el numero menor es: ", menor)  
  print("######################################################")  
