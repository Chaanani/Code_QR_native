from Data_coding import *
from operator import xor
def detrmine_bloc(chaine, niveau_correction):


 
  """
  cette fonction  permet de 
  déterminer le nombre du groupe 
  et ainsi que les nombres des blocs 
  dans chaque groupe 
  requis pour ce code QR 

  Parametrs:
  parametrs.
  chaine: the string we want to encoder.
  Niveau_correction: this is the level of correction
  """
 

  liste_groupe1=[]
  liste_groupe2=[]

  nombre_bloc_group1_L=[1,1,1,1,1,2,2,2,2,2,4,2,4,3,5,5,1,5,3,3,4,2,4,6,8,10,8,3,7,5,13,17,17,13,12,6,17,4,20,19]
  nombre_mots_group1_L=[19,34,55,80,108,68,78,97,116,68,81,92,107,115,87,98,107,120,113,107,116,111,121,117,106,114,122,117,116,115,115,115,115,115,121,121,122,122,117,118]
  
  nombre_bloc_group2_L=[0,0,0,0,0,0,0,0,0,2,0,2,0,1,1,1,5,1,4,5,4,7,5,4,4,2,4,10,7,10,3,0,1,6,7,14,4,18,4,6]

  nombre_bloc_group1_M=[1,1,1,2,2,4,4,2,3,4,1,6,8,4,5,7,10,9,3,3,17,17,4,6,8,19,22,3,21,19,2,10,14,14,12,6,29,13,40,18]
  nombre_mots_group1_M=[16,28,44,32,43,27,31,38,36,43,50,36,37,40,41,45,46,43,44,41,42,46,47,45,47,46,45,45,45,47,46,46,46,46,47,47,46,46,47,47]
  
  nombre_bloc_group2_M=[0,0,0,0,0,0,0,2,2,1,4,2,1,5,5,3,1,4,11,13,0,0,14,14,13,4,3,23,7,10,29,23,21,23,26,34,14,32,7,31]

  nombre_bloc_group1_Q=[1,1,2,2,2,4,2,4,4,6,4,4,8,11,5,15,1,17,17,15,17,7,11,11,7,28,8,4,1,15,42,10,29,44,39,46,49,48,43,34]
  nombre_mots_group1_Q=[13,22,17,24,15,19,14,18,16,19,22,20,20,16,24,19,22,22,21,24,22,24,24,24,24,22,23,24,23,24,24,24,24,24,24,24,24,24,24,24]
  nombre_bloc_group2_Q=[0,0,0,0,2,0,4,2,4,2,4,6,4,5,7,2,15,1,4,5,6,16,14,16,22,6,26,31,37,25,1,35,19,7,14,10,10,14,22,34]

  nombre_bloc_group1_H=[1,1,2,4,2,4,4,4,4,6,3,7,12,11,11,3,2,2,9,15,19,34,16,30,22,33,12,11,19,23,23,19,11,59,22,2,24,42,10,20]
  nombre_mots_group1_H=[9,16,13,9,11,15,13,14,12,15,12,14,11,12,12,15,14,14,13,15,16,13,15,16,15,16,15,15,15,15,15,15,15,16,15,15,15,15,15,15]
  nombre_bloc_group2_H=[0,0,0,0,12,0  ,14,2, 13, 16, 13 ,15, 12 ,  13 , 13 ,16 , 15 , 15 , 14 , 16 ,  17 , 0  , 16 ,  17 , 16  , 17 , 16  ,  16  ,  16  ,  16  ,  16  ,16 , 17  ,17, 16   ,16  ,16  ,16  ,16]
  
  nombre_mots_group2_L=[0,0,0,0,0, 0  ,0,  0,  0, 69,  0 ,93,  0 , 116 , 88 ,99 ,108 ,121 ,114 ,108 , 117 ,112 ,122 , 118 ,107  ,115 ,123  , 118  , 117  , 116  , 116  ,0   ,116 ,116, 122,122  ,123 ,123 ,118 ,119]
  nombre_mots_group2_M=[0,0,0,0,0, 0  ,0, 39 ,37, 44, 51, 37, 38 ,  41 , 42 ,46 , 47 , 44 , 45 , 42 ,   0 , 0  , 48 ,  46 , 48  , 47 , 46  ,  46  ,  46  ,  48  ,  47  ,47 , 47  ,47, 48  ,48 ,47  ,47  ,48  , 48]
  nombre_mots_group2_Q=[0,0,0,0,16,0  ,15,19, 17, 20, 23 ,21, 21,   17 , 25 ,20 , 23 , 23 , 22 , 25 ,  23 ,25  , 25 ,  25 , 25  , 23 , 24  ,  25  ,  24  ,  25  ,  25  ,25 , 25  ,25, 25  ,25 ,25  ,25  ,25   ,25]
  nombre_mots_group2_H=[0,0,0,0,12,0  ,14,15, 13, 16, 13 ,15, 12 ,  13 , 13 ,16 , 15 , 15 , 14 , 16 ,  17 , 0  , 16 ,  17 , 16  , 17 , 16  ,  16  ,  16  ,  16  ,  16 ,16, 16 ,17, 16  ,16 ,16  ,16  ,16  ,16]
  Data=Ecoding_data(chaine,niveau_correction)
  version=detrmine_version(chaine, niveau_correction)
  if niveau_correction=="L":
    nombre_bloc_groupe1=nombre_bloc_group1_L[version-1]
    nombre_mots_groupe1=nombre_mots_group1_L[version-1]
    nombre_bloc_groupe2=nombre_bloc_group2_L[version-1]
    nombre_mots_groupe2=nombre_mots_group2_L[version-1]

    i=1
    j=0
    while i<=nombre_bloc_groupe1:
      liste_groupe1.append(Data[j:8*nombre_mots_groupe1+j])
      j=8*nombre_mots_groupe1+j
      i=i+1
    if not(nombre_bloc_groupe2==0):
      k=1
      r=j
      while k<=nombre_bloc_groupe2:
        liste_groupe2.append(Data[r:8*nombre_mots_groupe2+r])
        r=8*nombre_mots_groupe2+r
        k=k+1

  if niveau_correction=="M":
    nombre_bloc_groupe1=nombre_bloc_group1_M[version-1]
    nombre_mots_groupe1=nombre_mots_group1_M[version-1]
    nombre_bloc_groupe2=nombre_bloc_group2_M[version-1]
    nombre_mots_groupe2=nombre_mots_group2_M[version-1] 
    i=1
    j=0
    while i<=nombre_bloc_groupe1:
      liste_groupe1.append(Data[j:8*nombre_mots_groupe1+j])
      j=8*nombre_mots_groupe1+j
      i=i+1
    if not(nombre_bloc_groupe2==0):
      k=1
      r=j
      while k<=nombre_bloc_groupe2:
        liste_groupe2.append(Data[r:8*nombre_mots_groupe2+r])
        r=8*nombre_mots_groupe2+r
        k=k+1 
  if niveau_correction=="Q":
    nombre_bloc_groupe1=nombre_bloc_group1_Q[version-1]
    nombre_mots_groupe1=nombre_mots_group1_Q[version-1]
    nombre_bloc_groupe2=nombre_bloc_group2_Q[version-1]
    nombre_mots_groupe2=nombre_mots_group2_Q[version-1]
    i=1
    j=0
    while i<=nombre_bloc_groupe1:
      liste_groupe1.append(Data[j:8*nombre_mots_groupe1+j])
      j=8*nombre_mots_groupe1+j
      i=i+1
    if not(nombre_bloc_groupe2==0):
      k=1
      r=j
      while k<=nombre_bloc_groupe2:
        liste_groupe2.append(Data[r:8*nombre_mots_groupe2+r])
        r=8*nombre_mots_groupe2+r
        k=k+1
  if niveau_correction=="H":

    nombre_bloc_groupe1=nombre_bloc_group1_H[version-1]
    nombre_mots_groupe1=nombre_mots_group1_H[version-1]
    nombre_bloc_groupe2=nombre_bloc_group2_H[version-1]
    nombre_mots_groupe2=nombre_mots_group2_H[version-1]
    i=1
    j=0
    while i<=nombre_bloc_groupe1:
      liste_groupe1.append(Data[j:8*nombre_mots_groupe1+j])
      j=8*nombre_mots_groupe1+j
      i=i+1
    if not(nombre_bloc_groupe2==0):
      k=1
      r=j
      while k<=nombre_bloc_groupe2:
        liste_groupe2.append(Data[r:8*nombre_mots_groupe2+r])
        r=8*nombre_mots_groupe2+r
        k=k+1
  resultat=[]
  
  for i in range(len(liste_groupe1)):
    m=0
    list_groupe1=[]
    while m<=len(liste_groupe1[i])-1:
      list_groupe1.append(liste_groupe1[i][m:m+8])
      m=m+8
    resultat.append(list_groupe1)
  resultat1=[]
  for i in range(len(liste_groupe2)):
    m=0
    list_groupe2=[]
    while m<=len(liste_groupe2[i])-1:
      list_groupe2.append(liste_groupe2[i][m:m+8])
      m=m+8
    resultat1.append(list_groupe2)  
  return resultat, resultat1


def Conversion():
  """
  cette fonction 
  permet de convertir les puissances de 2 
  """
  xorko=[1,2,4,8,16,32,64,128,29]
  for i in range(9,256):
    if 2*xorko[-1]<255: 
      xorko.append(2*xorko[-1])
    else :
      xorko.append(xor(2*xorko[-1],285))
  return xorko


def log(liste):
  """Cette methode permets de convertir
  les entiers  sous forme de 2^{i}"""
  
  sortie=[]
  for k in liste:
    for i, j in zip(Conversion(),range(256)):
      if k==i:
        sortie.append(j)
        break
  return sortie

def antilog(liste):
  """Cette methode fait l'inverse de la fonction log"""
  sortie=[]
  for i in liste:
    sortie.append(Conversion()[i])
  return sortie

def produit(a,b):

  """
  Cette methode fait le produit entre de polynomes

  parametrs:

  a= liste des coeficients du premier  polynomes
  b= liste des coeficients du deuxieme  polynomes  
  """
  resultat=[]
  for i in range(len(a)+len(b)-1):
    resultat.append(0)
  for i in range(len(a)):
    for j in range(len(b)):
       if a[i]+b[j]>=255:
         d=a[i]+b[j]
         c=d%255
         for z in antilog([c]):
           resultat[i+j]=xor(resultat[i+j],z)
       else:
         for z in antilog([a[i]+b[j]]):
           resultat[i+j]=xor(resultat[i+j],z)
  return resultat

def Generator_poly(k):
   """
   Cette methode permet calculer le polynome generateur

   paramerts
   k : est le degré de polynome genérateur
   """
   r=[0,0]
   h=[0]
   for i in range(k-1):
     h.append(i+1)
     r=produit(r,h)
     r=log(r)
     h=[0]
   return r

def Erreur_Correction(message,nbre_correction):
  """
  cette fonction fait la division eucludienne 
  dans le groupe de galois de 255

  parametrs:

  message: le message des données 

  nbre_correction : le nombre de correction c'est a 
  dire le degré du polynome generatrice
  """

  message=message
  lenmessage=len(message)
  polynome_generatrice_puissance=Generator_poly(nbre_correction)
  polynome_message_puissancee=log(message)
  for j in range(nbre_correction):
      message.append(0)
  k=0
  while k<lenmessage:
    for i in range(len(polynome_generatrice_puissance)):
      if polynome_generatrice_puissance[i]+polynome_message_puissancee[0]<255:
        polynome_generatrice_puissance[i]=polynome_generatrice_puissance[i]+polynome_message_puissancee[0] 
      else:
        polynome_generatrice_puissance[i]=(polynome_generatrice_puissance[i]+polynome_message_puissancee[0])%255
    polynome_generatrice_dicimal=antilog(polynome_generatrice_puissance)
    for l in range(len(message)-len(polynome_generatrice_dicimal)):
      polynome_generatrice_dicimal.append(0)
    resultat=[]
    for m, n in zip(message,polynome_generatrice_dicimal):
        resultat.append(xor(m,n))
    del resultat[0]
    if resultat[0]==0:
      del resultat[0]
      message=resultat
      polynome_message_puissancee=log(message)
      polynome_generatrice_puissance=Generator_poly(nbre_correction) 
      k=k+2 
    elif not(resultat[0]==0):
      message=resultat
      polynome_message_puissancee=log(message)
      polynome_generatrice_puissance=Generator_poly(nbre_correction) 
      k=k+1
  return message

def covrrt(liste):
  """
  cette methode convertir une liste de
  binaire en forme entiere 
  """
  test=[]
  for i in liste:
    test.append(int(i,2))
  return test  
def covv(liste):
  """
  cette methode convertir une 
  liste de forme entiere en forme binaire 
  """
  sorti=[]
  for i in liste:
    x=format(i,'b')
    sorti.append((8-len(x))*'0'+x)
  return sorti


def Reed_Correction(chaine,niveau_correction):

  """cette methode qui prend tous les blocs dans 
  chaque groupe et apres elle fait la divison 
  eucludienne de chaque bloc
  
  parametrs:

  chaine: la chaine du message
  niveau_correction: niveau de correction soit L, M, Q, H

  """


  resultat=[]
  resultat1=[]
  version=detrmine_version(chaine,niveau_correction)
  data=detrmine_bloc(chaine,niveau_correction)
  degre_poly_genera_L=[7, 10, 15,20,26,18,20,24,30,18, 20, 24, 26, 30,  22,  24, 28, 30,  28,  28,  28,  28,    30,   30,    26,  28,  30,   28,  30,    30,    30,    30,    30,  30,  30, 30, 30, 30,  30,  30]
  degre_poly_genera_M=[10,16, 26,18,24,16,18,22,22,26, 30 ,22, 22, 24,  24,  28, 28, 26,  26,  26,   26,  28,   28,   28,    28,  28,  28,   30,  28,    28,     28,    28,    28,  28,  28, 28, 28, 28,  28,  28]
  degre_poly_genera_Q=[13,22, 18,26,18,24,18,22,20 ,24, 28 ,26, 24, 20 , 30,  24, 28, 28,  26,  30,   28,  30,   30,   30,    30,  28,  30,   30,  30,    30,     30,    30,    30,  30,  30, 30, 30, 30,  30,  30]
  degre_poly_genera_H=[17,28, 22,16,22,28,26,26,24 ,28, 24 ,28, 22, 24 , 24,  30, 28, 28,  26,  28,   30,  24,   30,   30,    30,  30,  30,   30,  30,    30,     30,    30,    30,  30,  30, 30, 30, 30,  30,  30]
  
  if niveau_correction=="L":
    degre_poly_genera= degre_poly_genera_L[version-1]

  if niveau_correction=="M":
    degre_poly_genera= degre_poly_genera_M[version-1]

  if niveau_correction=="Q":
    degre_poly_genera= degre_poly_genera_Q[version-1]

  if niveau_correction=="H":
    degre_poly_genera= degre_poly_genera_H[version-1]
  for i in data[0]:
    z=covrrt(i)
    et=Erreur_Correction(z,degre_poly_genera)
    resultat.append(et)
  if not(len(data[1])==0):
    for r in data[1]:
      e=covrrt(r)
      zt=Erreur_Correction(e,degre_poly_genera)
      resultat1.append(zt)


  return resultat, resultat1
