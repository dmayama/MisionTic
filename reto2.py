n = int(input('Cantidad de muestras '))
i = 1
acidez_acumulada = 0
ca_acumulada = 0
s_apto = 0
mod_apto = 0
mar_apto = 0
no_apto = 0
while i <= n:
  acidez = float(input('Ingrese la acidez (PH) '))
  acidez_acumulada += acidez
  ca = float(input('Ingrese el Ca(meg/100gr) '))
  ca_acumulada += ca
  i2 = 0

  if 6.5 > acidez >= 5.5 and 4 > ca > 2: 
    i2 = 1
    s_apto += 1

  if (7 > acidez >= 6.5 or 5.5 > acidez >= 5) and (8 > ca >= 4): 
    i2 = 1
    mod_apto += 1

  if (8 > acidez >= 7 or 5 > acidez > 4.5) and (12 > ca >= 8):
    i2 = 1 
    mar_apto += 1 

  if (acidez > 8 or acidez < 4.5)  and (ca > 12 or ca < 2): 
    i2 = 1
    no_apto += 1

  if i2 == 0:
    if (acidez > 8 or acidez < 4.5)  or (ca > 12 or ca < 2): 
      no_apto += 1
    elif (8 > acidez >= 7 or 5 > acidez > 4.5) or (12 > ca >= 8):
      mar_apto += 1 
    elif (7 > acidez >= 6.5 or 5.5 > acidez >= 5) or (8 > ca >= 4):
      mod_apto += 1
    elif 6.5 > acidez >= 5.5 or 4 > ca > 2: 
      s_apto += 1

  i += 1
prom_a = acidez_acumulada/n
prom_ca = ca_acumulada/n
print(round(prom_a, 2))
print(round(prom_ca, 2))
print('sumamente apto ',s_apto)
print('moderadamente apto ',mod_apto)
print('marginamente apto ',mar_apto)
print('no apto ',no_apto)