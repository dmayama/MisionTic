def crear_matriz(n):
  matriz = []
  listas = 1
  filas = 2*n
  while listas <= filas:
    valor = input(' ').split()
    longitud = len(valor)
    fila = []
    for j in range (longitud):
      fila.append(valor[j])
    matriz.append(fila)
    listas += 1
  return (matriz)
def imp_resultados(lista_max,lista_min,s_apto_acum,mod_apto_acum,mar_apto_acum,no_apto_acum):
  print(f'No apto {no_apto_acum}, Marginalmente apto {mar_apto_acum}, moderadamente apto {mod_apto_acum}, Sumamente apto {s_apto_acum}')
  print ('Los resultados mas repetidos por zona son: ')
  print (','.join(lista_max))
  print ('Los resultados menos repetidos por zona son: ')
  print (','.join(lista_min))

def lista_max_min(lista_max,lista_min,s_apto,mod_apto,mar_apto,no_apto):
  lista_entrada=[s_apto,mod_apto,mar_apto,no_apto]
  evaluador = min(lista_entrada)
  rep = 0
  for pos in range(len(lista_entrada)):
    if (lista_entrada[pos] > evaluador) and lista_entrada[pos] != 0 :
      evaluador = lista_entrada[pos]
  if (lista_entrada[0] == evaluador) and rep == 0:
    rep+=1
    max_min ='sumamente apto'
  elif (lista_entrada[1] == evaluador) and rep == 0:
    rep+=1
    max_min ='moderadamente apto'
  elif (lista_entrada[2] == evaluador) and rep == 0:
    rep+=1
    max_min ='marginalmente apto'
  elif (lista_entrada[3] == evaluador) and rep == 0:
    rep+=1
    max_min ='no apto'
  lista_max.append(max_min)
  evaluador = max(lista_entrada)
  rep=0
  for pos2 in range(len(lista_entrada)):
    if (lista_entrada[pos2] < evaluador) and lista_entrada[pos2] != 0 :
      evaluador = lista_entrada[pos2]
  if (lista_entrada[0] == evaluador) and rep == 0:
    rep+=1
    max_min ='sumamente apto'
  elif (lista_entrada[1] == evaluador) and rep == 0:
    rep+=1
    max_min ='moderadamente apto'
  elif (lista_entrada[2] == evaluador) and rep == 0:
    rep+=1
    max_min ='marginalmente apto'
  elif (lista_entrada[3] == evaluador) and rep == 0:
    rep+=1
    max_min ='no apto'
  lista_min.append(max_min)
  return(lista_max,lista_min)

def evaluar(acidez_prom, ca_prom,s_apto,mod_apto,mar_apto,no_apto):
  i2 = 0 

  if (5.50 < acidez_prom <= 6.50) and (2 <= ca_prom <= 4): 
    i2 = 1
    s_apto += 1

  elif (6.50 < acidez_prom <= 7 or 5 <= acidez_prom < 5) and (8 >= ca_prom > 4): 
    i2 = 1
    mod_apto += 1

  elif (8 >= acidez_prom > 7 or 5 >= acidez_prom >= 4.50) and (12 >= ca_prom > 8):
    i2 = 1 
    mar_apto += 1 

  elif (acidez_prom > 8 or acidez_prom < 4.50)  and (ca_prom > 12 or ca_prom < 2): 
    i2 = 1
    no_apto += 1

  if i2 == 0:
    if (acidez_prom > 8) or (acidez_prom < 4.50)  or (ca_prom > 12 or ca_prom < 2): 
      no_apto += 1
    elif (8 >= acidez_prom > 7) or (5 >= acidez_prom >= 4.50) or (12 >= ca_prom > 8):
      mar_apto += 1 
    elif (7 >= acidez_prom > 6.50 ) or (5.50 >= acidez_prom > 5) or (8 >= ca_prom > 4):
      mod_apto += 1
    elif (6.50 >= acidez_prom > 5.50) or (4 >= ca_prom >= 2): 
      s_apto += 1
  return(s_apto,mod_apto,mar_apto,no_apto)

def reto4():
  n = int(input('Ingrese el numero de zonas a evaluar: '))
  lista_max = []
  lista_min = []
  matriz = crear_matriz(n)
  s_apto_acum = 0 
  mod_apto_acum = 0 
  mar_apto_acum = 0 
  no_apto_acum = 0
  s_apto = 0
  mod_apto = 0
  mar_apto = 0
  no_apto = 0
  filalec1 = 0
  filalec2 = n
  z=0
  while z < n:
    for columna in range(len(matriz[1])):
      acidez_prom = float(matriz[filalec1][columna])
      ca_prom = float(matriz[filalec2][columna])
      (s_apto,mod_apto,mar_apto,no_apto)=evaluar(acidez_prom,ca_prom,s_apto,mod_apto,mar_apto,no_apto)
    (lista_max,lista_min)=lista_max_min(lista_max,lista_min,s_apto,mod_apto,mar_apto,no_apto)
    s_apto_acum += s_apto
    mod_apto_acum += mod_apto
    mar_apto_acum += mar_apto
    no_apto_acum += no_apto
    s_apto = 0
    mod_apto = 0
    mar_apto = 0
    no_apto = 0
    filalec1 += 1
    filalec2 += 1
    z += 1
  imp_resultados(lista_max,lista_min,s_apto_acum,mod_apto_acum,mar_apto_acum,no_apto_acum)
reto4()