import math
from Module_Placement import *
from Penalty import *
from Chaine_version import *
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def sauter(matrice,i,j,alignement):
  """
  Cette methode qui permets de sauter 
  les modeles d'alignement et  fait le masquage 

  parametrs:
    
  matrice: la matrice sur laquelle on applique le mask

  i,j: c'est les indices de pixel qu'on peut masquer

  aligement: c'est le centre  du modele d'alignement qu'on peut sauter
  """

  n=matrice.shape[0]
  Center=[]
  for h in alignement: 
    #ici c'est grand probleme
    if (((0<=h[0]-2<=8) and (0<=h[1]-2<=8)) or ((n-8<= h[0]+3<=n-1) and (0<=h[1]-2<=8)) or((0<= h[0]-2<=8) and (n-8<=h[1]+3<=n-1))) ==False:
      Center.append(h)
  for x in Center:
    if not(x[1]-2<=i<=x[1]+3 and x[0]-2<=j<=x[0]+3):
      if matrice[i,j]==1:
          matrice[i,j]=0
      else:
         matrice[i,j]=1


def masque(numbre,i,j,matrice,alignement):
  """
  cette methode fait le masquage selon le numbre du mask
   

  parametrs:
  numbre:  c'est le nombre de mask
  i,j : c'est les pixel qu'on peut masquer
  matrice: c'est la matrice sur laquelle on applique le mask
  alignement: c'est le centre du modele qu'on peut sauter lors du masquage

  """
  if numbre==0:
    if (i+j)%2==0:
      sauter(matrice,i,j,alignement)
  elif numbre==1:
    if i%2==0:
      sauter(matrice,i,j,alignement)
  elif numbre==2:
    if j%3==0:
       sauter(matrice,i,j,alignement)
  elif numbre==3:
    if (i+j)%3==0:
      sauter(matrice,i,j,alignement)
  elif numbre==4:
    if (math.floor(i/2) + math.floor(j/3))% 2 == 0:
      sauter(matrice,i,j,alignement)
  elif numbre==5:
    if ((i*j)%2+(i*j)%3)==0:
      sauter(matrice,i,j,alignement)
  elif numbre==6:
    if ((i*j)%2+(i*j)%3)%2==0:
      sauter(matrice,i,j,alignement)
  elif numbre==7:
    if ((i+j)%2+(i*j)%3)%2==0:
      sauter(matrice,i,j,alignement)






import math
def mask(chaine,niveau_correction,numbre_masque):

  """
  cette methode génére la  matrice du code QR et fait le masquage

  parametrs:

  chaine: c'est la chaine de caractere sur laquelle on génére le code QR
  niveau_correction: le niveau de correction du code QR 

  numbre_masque: c'est le nombre de masque
  """
  version=detrmine_version(chaine,niveau_correction)
  alignement=Alignement[version-1]
  matrice=Placement(chaine,niveau_correction)
  numbre_masque=numbre_masque
  
  n=matrice.shape[0]
  if version<6:
    for i in range(9):
      for j in range(9,n-8):
        if not(i==6):
          masque(numbre_masque,i,j,matrice,alignement)
    for i in range(9,n-8):
      for j in range(n):
        if not(j==6):
          masque(numbre_masque,i,j,matrice,alignement)
    
    for i in range(n-8,n):
      for j in range(9,n):
        masque(numbre_masque,i,j,matrice,alignement)
  
    
  else:
    for i in range(6):
      for j in range(8,n-11):
          masque(numbre_masque,i,j,matrice,alignement)
    for i in range(7, 8):
      for j in range(8,n-8):
          masque(numbre_masque,i,j,matrice,alignement)
      
    for i in range(8, n-11):
      for j in range(6):
        masque(numbre_masque,i,j,matrice,alignement)
    for i in range(9, n-8):
      for j in range(7,8):
          masque(numbre_masque,i,j,matrice,alignement)
  
    for i in range(n-8,n):
      for j in range(8,n):
        masque(numbre_masque,i,j,matrice,alignement)

  return matrice



#################################
#################################

def final_qr(chaine,niveau_correction):
  score=[]
  for i in range(8):
    score.append(total_penalty(mask(chaine,niveau_correction,i)))
  z=score.index(min(score))
  return mask(chaine,niveau_correction,z),z


def QRRRR(chaine,niveau_correction):
  matrice=final_qr(chaine,niveau_correction)
  matrice1=mask(chaine,niveau_correction,2)
  nbre_masque=2
  print("numbre of mask",nbre_masque)
  version=detrmine_version(chaine, niveau_correction)
  n=(version-1)*4+21
  if version<7:
    bits_version=chaine_format_6(niveau_correction,nbre_masque)
    resultat=[]
    for j in bits_version:
      resultat.append(j)
    
    for i in range(9):
      if not(i==6):
        matrice1[i,8]=int(resultat[-1])
        del resultat[-1]
    for i in range(8):
      if not(i==6):
        matrice1[8,i]=int(resultat[0])
        del resultat[0]
    rest=[]
    for j in bits_version:
      rest.append(j)
    for i in range(8):
      matrice1[8,n-1-i]=int(rest[-1])
      del rest[-1]
    for i in range(7):
      matrice1[n-1-i,8]=int(rest[-1])
      del rest[-1]

  else:
    bits_version=chaine_format_7(version)
  return matrice1

