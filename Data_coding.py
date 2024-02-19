def detrmine_version(chaine,niveau_correction):
     """this function which allows
     to determine the version of the QR code.
    
     parametrs:
     chaine: the string we want to encoder.
     niveau_correction: this is the level of correction
     
     """
     L=[17,32,53,78,106,134,154,192,230,271,321,367,425,458,520,586,644,718,792,858,929,1003,1091,1171,1273,1367,1465,1528,1628,1732,1840,1952,2068,2188,2303,2431,2563,2699,2809,2953]
     M=[14,26,42,62,84,106,122,152,180,213,251,287,331,362,412,450,504,560,624,666,711,779,857,911,997,1059,1125,1190,1264,1310,1452,1538,1628,1722,1809,1911,1989,2099,2213,2331]
     Q=[11,20,32,46,60,74,86,108,130,151,177,203,241,258,292,322,364,394,442,482,509,565,611,661,715,751,805,868,908,982,1030,1112,1168,1228,1283,1351,1423,1499,1579,1663]
     H=[7,14,24,34,44,58,64,84,98,119,137,155,177,194,220,250,280,310,338,382,403,439,461,511,535,593,625,658,698,742,790,842,898,958,983,1051,1093,1139,1219,1273]
     longeur_chaine=len(chaine)
     
     if niveau_correction=="L":
       for i,j in enumerate(L):
         if longeur_chaine<=j:
           return i+1
           break
     elif niveau_correction=="M":
      
       for i,j in enumerate(M):
         if longeur_chaine<=j:
           return i+1
           break
     elif niveau_correction=="Q":
      
       for i,j in enumerate(Q):
         if longeur_chaine<=j:
           return i+1
           break
     elif niveau_correction=="H":
     
       for i,j in enumerate(H):
         if longeur_chaine<=j:
           return i+1
           break


def Count_indicator(chaine,niveau_correction):

  """this function which allows to 
  add the character indicator.
  parametrs.
  chaine: the string we want to encoder.
  Niveau_correction: this is the level of correction
  """

  version=detrmine_version(chaine,niveau_correction)
  longueur=len(chaine)
  longueur_binaire=format(longueur,'b')
  longueur_binaire=str(longueur_binaire)
  if 1<=version<=9:
    longueur_binaire=(8-len(longueur_binaire))*'0'+longueur_binaire
  elif 10<=version<=26:
    longueur_binaire=(16-len(longueur_binaire))*'0'+longueur_binaire
  elif 27<=version<=40:
    longueur_binaire=(16-len(longueur_binaire))*'0'+longueur_binaire
  
  longueur_binaire='0100'+longueur_binaire 
  return longueur_binaire


def Encoder(chaine,niveau_correction):
  """
  this method which allows to code 
  the strings in the form of bytes.

  parametrs.
  chaine: the string we want to encoder.
  Niveau_correction: this is the level of correction
  """
  t=''
  for x in bytearray(chaine, 'utf-8'):
   z=''.join(format(x, 'b'))
   z=(8-len(z))*'0'+z
   t=t+z
  return Count_indicator(chaine,niveau_correction)+t


def Determine_Numbre_bite(chaine,niveau_correction):
  """
  cette fonction qui permet de 
  déterminer le nombre de bits 
  requis pour ce code QR et ajoutée les zéros a la fin si nécessaire

  Parametrs:
  parametrs.
  chaine: the string we want to encoder.
  Niveau_correction: this is the level of correction
  """
  
  Nombre_total_L=[19,34,55,80,108,136,156,194,232,274,324,370,428,461,523,589,647,721,795,861,932,1006,1094,1174,1276,1370,1468,1531,1631,1735,1843,1955,2071,2191,2306,2434,2566,2702,2812,2956]
  Nombre_total_M=[16,28,44,64,86,108,124,154,182,216,254,290,334,365,415,453,507,563,627,669,714,782,860,914,1000,1062,1128,1193,1267,1373,1455,1541,1631,1725,1812,1914,1992,2102,2216,2334]
  Nombre_total_Q=[13,22,34,48,62,76,88,110,132,154,180,206,244,261,295,325,367,397,445,485,512,568,614,664,718,754,808,871,911,985,1033,1115,1171,1231,1286,1354,1426,1502,1582,1666]
  Nombre_total_H=[9,16,26,36,46,60,66,86,100,122,140,158,180,197,223,253,283,313,341,385,406,442,464,514,538,596,628,661,701,745,793,793,845,901,961,986,1054,1096,1142,1222,1276]

  version=detrmine_version(chaine,niveau_correction)
  if niveau_correction=="L":
    nombre_bits=Nombre_total_L[version-1] 
  if niveau_correction=="M":
    nombre_bits=Nombre_total_M[version-1]  
  if niveau_correction=="Q":
    nombre_bits=Nombre_total_Q[version-1] 
  if niveau_correction=="H":
    nombre_bits=Nombre_total_H[version-1]
  codage=Encoder(chaine,niveau_correction)
  
  if nombre_bits*8-len(codage)>=4:
    codage=codage+4*'0'
  
  if (nombre_bits*8-len(codage)<4 ==True):
    codage=codage+'0'
  return codage, nombre_bits*8

def add_zeros(chaine,niveau_correction):
  """cette fonction fait les zeros a la ffin du code si necéssaire
  
  parametrs.
  chaine: the string we want to encoder.
  Niveau_correction: this is the level of correction
  
  """

  codage=Determine_Numbre_bite(chaine,niveau_correction)[0]
  longueurr=len(codage)
  longueur=longueurr%8
  if longueur==0:
    return codage
  else:
    resultat=8-longueur
    codage=codage+resultat*'0'
    return codage


def Ecoding_data(chaine,niveau_correction):
  """cette fonction permet ajouter les "11101100 00010001" a la fin du code si necéssaire
  
  parametrs.
  chaine: the string we want to encoder.
  Niveau_correction: this is the level of correction
  
  """
  long_bits=Determine_Numbre_bite(chaine,niveau_correction)[1]
  code=add_zeros(chaine, niveau_correction)
  long_bits=long_bits-len(code)

  rt=long_bits//8 

  listte=['11101100','00010001']
  i=1
  while i<=rt:
    if not(i%2==0):
      code=code+listte[0]
    else:
      code=code+listte[1]
    i=i+1
  return code



