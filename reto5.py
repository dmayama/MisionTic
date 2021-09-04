import csv
def leer_datos():
  valor = []
  with open("data.csv", 'r') as data:#open('Que archivo', 'Que hacer')
    for line in csv.reader(data):
      valor.append(line)
  return(valor)
def crear_matriz(valor,ciudad):
  matriz = valor
  matriz_2 = []
  fila_2 = 0
  while fila_2 < len(matriz):
    evaluar = str(matriz[fila_2][0])
    if (evaluar) == ciudad:
      fila_lista = []
      for columna_3 in range (len(matriz[1])):
        dato = matriz[fila_2][columna_3]
        fila_lista.append(dato)
      matriz_2.append(fila_lista)
    fila_2 += 1
  return (matriz_2)
def evaluar(tipo,s_apto,mod_apto,mar_apto,no_apto):
  if tipo =='sumamente apto': 
    s_apto += 1

  if tipo == 'moderadamente apto': 
    
    mod_apto += 1

  if tipo == 'marginalmente apto':
    
    mar_apto += 1 

  if tipo == 'no apto': 

    no_apto += 1

  return(s_apto,mod_apto,mar_apto,no_apto)
def lista_max_min(lista_ca,lista_acidez):
  evaluador_ca = max(lista_ca)
  evaluador_acidez = max(lista_acidez)
  maximo=[evaluador_acidez,evaluador_ca]
  for pos in range(len(lista_acidez)):
    if (lista_acidez[pos] < evaluador_acidez) and lista_acidez[pos] != 0 :
      evaluador_acidez = lista_acidez[pos]
  for pos in range(len(lista_ca)):
    if (lista_ca[pos] < evaluador_ca) and lista_ca[pos] != 0 :
      evaluador_ca = lista_ca[pos]
  minimo=[evaluador_acidez,evaluador_ca]
  return(maximo,minimo)
def imp_resultados(matriz, ca_sum, acidez_sum, lista_max,lista_min,s_apto,mod_apto,mar_apto,no_apto):
  print('Los poromedios de acidez y ca de la ciudad elegida es: ')
  print("{0:.2f}".format(acidez_sum/len(matriz)),"{0:.2f}".format(ca_sum/len(matriz)))
  print('Los valores minimos son: ')
  for imp_c in range(len(lista_min)):
    print(lista_min[imp_c], end=' ')
  print (' ')
  print('Los valores maximos son: ')
  for imp_c in range(len(lista_max)):
    print(lista_max[imp_c], end=' ')
  print(' ')
  lista_datos = [no_apto,mar_apto,mod_apto,s_apto]
  metodo = 0
  for pos in range (len(lista_datos)):
    var = lista_datos[pos]   
    if max(lista_datos) == var:
      if pos == 0:
        print(f'no apto {no_apto}')
        metodo += 1
      if pos == 1:
        print(f'marginalmente apto {mar_apto}')
        metodo += 1
      if pos == 2: 
        print(f'moderadamente apto {mod_apto}')
        metodo += 1
      if pos == 3:
        print(f'sumamente apto {s_apto}')
        metodo += 1
    medios = sum(lista_datos)-max(lista_datos)-min(lista_datos)
    medio = medios-var
    if var != max(lista_datos) and var != min(lista_datos):
      if var > medio and pos == 0:
        print(f'no apto {no_apto}')
        metodo += 1
      if var > medio and pos == 1:
        print(f'marginalmente apto {mar_apto}')
        metodo += 1
      if var > medio and pos == 2: 
        print(f'moderadamente apto {mod_apto}')
        metodo += 1     
      if var > medio and pos == 3:
        print(f'sumamente apto {s_apto}')
        metodo += 1
      if var < medio and pos == 0:
        print(f'no apto {no_apto}')
        metodo += 1
      if var < medio and pos == 1:
        print(f'marginalmente apto {mar_apto}')
        metodo += 1
      if var < medio and pos == 2: 
        print(f'moderadamente apto {mod_apto}')
        metodo += 1
      if var < medio and pos == 3:
        print(f'sumamente apto {s_apto}')
        metodo += 1
    if var == min(lista_datos) and pos == 0:
      print(f'no apto {no_apto}')
      metodo += 1
    if var == min(lista_datos) and pos == 1:
      print(f'marginalmente apto {mar_apto}')
      metodo += 1
    if var == min(lista_datos) and pos == 2: 
      print(f'moderadamente apto {mod_apto}')
      metodo += 1
    if var == min(lista_datos) and pos == 3:
      print(f'sumamente apto {s_apto}')
      metodo += 1
    if var == medio and var == max(lista_datos) and var == min(lista_datos) and metodo == 0:
      print(f'marginalmente apto {mar_apto}')
      print(f'moderadamente apto {mod_apto}')
      print(f'no apto {no_apto}')
      print(f'sumamente apto {s_apto}')
def reto4():
    ciudad = str(input(''))
    valor = leer_datos()
    lista_max = []
    lista_min = []
    matriz = crear_matriz(valor,ciudad)
    s_apto = 0
    mod_apto = 0
    mar_apto = 0
    no_apto = 0
    acidez_sum = 0
    ca_sum = 0
    filalec1 = 1
    filalec2 = len(matriz)
    n = len(matriz)
    z=0
    lista_acidez=[]
    lista_ca=[]
    while z < n:
      acidez_prom = float(matriz[z][2])
      acidez_sum += acidez_prom
      lista_acidez.append(acidez_prom)
      ca_prom = float(matriz[z][5])
      ca_sum += ca_prom
      lista_ca.append(ca_prom)
      tipo = matriz[z][6]
      (s_apto,mod_apto,mar_apto,no_apto)=evaluar(tipo,s_apto,mod_apto,mar_apto,no_apto)
      (lista_max,lista_min)=lista_max_min(lista_ca,lista_acidez)
      filalec1 += 1
      filalec2 += 1
      z += 1
    imp_resultados(matriz, ca_sum, acidez_sum, lista_max,lista_min,s_apto,mod_apto,mar_apto,no_apto)
reto4()