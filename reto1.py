acidez = float(input('Ingrese la acidez (PH) '))
ca = float(input('Ingrese el Ca(meg/100gr) '))
i=0;
if 6.5 >= acidez >= 5.6 and 4 >= ca >= 2: 
    print('Sumamente apto')
    i=1;

if (7 >= acidez >= 6.6 or 5.5 >= acidez >= 5.1) and (8 > ca > 4.1): 
    print('Moderadamente apto')
    i=1;

if (8 >= acidez >= 7.1 or 5 >= acidez >= 4.5) and (12 > ca > 8.1):
    print('Marginalmente apto')
    i=1;  

if (acidez > 8 or acidez < 4.5)  and (ca > 12 or ca < 2): 
    print('No apto') 
    i=1;

if i == 0:
  if (acidez > 8 or acidez < 4.5)  or (ca > 12 or ca < 2): 
    print('No apto')
  elif (8 >= acidez >= 7.1 or 5 >= acidez >= 4.5) or (12 >= ca >= 8.1):
    print('Marginalmente apto')
  elif (7 >= acidez >= 6.6 or 5.5 >= acidez >= 5.1) or (8 >= ca >= 4.1):
    print('Moderadamente apto')
  elif 6.5 >= acidez >= 5.6 or 4 >= ca >= 2:
    print('Sumamente apto') 