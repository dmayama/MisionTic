def imp_resultados(s_apto,mod_apto,mar_apto,no_apto):
  print('sumamente apto ',s_apto)
  print('moderadamente apto ',mod_apto)
  print('marginalmente apto ',mar_apto)
  print('no apto',no_apto)
def reto3():
  n = int(input('Cantidad de suelos a evaluar '))
  i = 1
  acidez_prom_lista=[]
  ca_prom_lista=[]
  s_apto = 0
  mod_apto = 0
  mar_apto = 0
  no_apto = 0
  while i <= n:
    acidez=[]
    ca=[]
    acidez_acumulada = 0
    ca_acumulada = 0
    acidez =input('Ingrese la acidez (PH) ').split()
    longitud=len(acidez)
    l1=0
    while l1<longitud:
      valor=float(acidez[l1])
      acidez_acumulada += valor
      l1+=1
    acidez_prom = acidez_acumulada/len(acidez)
    acidez_prom_lista.append(acidez_prom)
    ca = input('Ingrese la Ca(meg/100gr) ').split()
    longitud=len(ca)
    l2=0
    while l2<longitud:
      valor=float(ca[l2])
      ca_acumulada += valor
      l2+=1
    ca_prom = ca_acumulada/len (ca)
    ca_prom_lista.append(ca_prom)
    i2 = 0 
    if 6.5 > acidez_prom >= 5.5 and 4 > ca_prom > 2: 
      i2 = 1
      s_apto += 1

    if (7 > acidez_prom >= 6.5 or 5.5 > acidez_prom >= 5) and (8 > ca_prom >= 4): 
      i2 = 1
      mod_apto += 1

    if (8 > acidez_prom >= 7 or 5 > acidez_prom > 4.5) and (12 > ca_prom >= 8):
      i2 = 1 
      mar_apto += 1 

    if (acidez_prom > 8 or acidez_prom < 4.5)  and (ca_prom > 12 or ca_prom < 2): 
      i2 = 1
      no_apto += 1

    if i2 == 0:
      if (acidez_prom > 8 or acidez_prom < 4.5)  or (ca_prom > 12 or ca_prom < 2): 
        no_apto += 1
      elif (8 > acidez_prom >= 7 or 5 > acidez_prom > 4.5) or (12 > ca_prom >= 8):
        mar_apto += 1 
      elif (7 > acidez_prom >= 6.5 or 5.5 > acidez_prom >= 5) or (8 > ca_prom >= 4):
        mod_apto += 1
      elif 6.5 > acidez_prom >= 5.5 or 4 > ca_prom > 2: 
        s_apto += 1
    i += 1
  for p1 in range(len(acidez_prom_lista)):
    valor1 = acidez_prom_lista[p1]
    print ('{:,.2f}'.format(valor1), end = ' ')
  print(' ')
  for p2 in range(len(ca_prom_lista)):
    valor2 = ca_prom_lista[p2]
    print ("{0:.2f}".format(valor2), end = ' ')
  print(' ')
  imp_resultados(s_apto,mod_apto,mar_apto,no_apto)
reto3()