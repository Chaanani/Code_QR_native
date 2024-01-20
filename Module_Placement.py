from Data_coding import *
import numpy as np
from Structure_Final_Message import *

Alignement=[[[2,2]],[[6,6],[6,18],[18,6],[18,18]]
  ,[[6,6],[6,22],[22,6],[22,22]]
  ,[[26,6],[6,26],[6,6],[26,26]]
  ,[[6,6],[30,6],[6,30],[30,30]]
  ,[[6,6],[6,34],[34,6],[34,34]]
  ,[[6,22],[22,38]]
  ,[ [6,24],[24,42]]
  ,[[6,26],[2,46]]
  ,[ [6,28],[28,50]]
  ,[ [6,30],[30,54]]
  ,[ [6,32],[32,58]]
  ,[ [6,34],[34,62]]
  ,[ [6,26],[26,46],[46,66]]
  ,[ [6,26],[26,48],[48,68]]
  ,[ [6,26],[26,50],[50,70]]
  ,[ [6,30],[30,54],[54,78]]
  ,[ [6,30],[30,56],[56,82]]
  ,[ [6,30],[30,58],[58,86]]
  ,[ [6,34],[34,62],[62,90]]
  ,[ [6,28],[28,50],[50,72],[72,94]]
  ,[ [6,26],[26,50],[50,74],[74,98]]
  ,[ [6,30],[30,54],[54,78],[78,104]]
  ,[ [6,28],[28,54],[54,80],[80,106]]
  ,[ [6,3],[32,58],[58,84],[84,110]]
  ,[ [6,30],[30,58],[58,86],[86,114]]
  ,[ [6,34],[34,62],[62,90],[90,118]]
  ,[ [6,26],[26,50],[50,74],[74,98],[98,122]]
  ,[ [6,30],[30,54],[54,78],[78,102],[102,126]]
  ,[ [6,26],[26,52],[52,78],[78,104],[104,130]]
  ,[ [6,30],[30,56],[56,82],[82,108],[108,134]]
  ,[ [6,34],[34,60],[60,86],[86,112],[112,138]]
  ,[ [6,30],[30,58],[58,86],[86,114],[114,142]]
  ,[[6,34],[34,62],[62,90],[90,118],[118,146]]
  ,[[6,30],[30,54],[54,78],[78,102],[102,126],[126,150]]  
  ,[[6,24],[24,50],[50,76],[76,102],[102,128],[128,154]]
  ,[[6,28],[28,54],[54,80],[80,104],[104,132],[132,158]]
  ,[[6,32],[32,58],[58,84],[84,110],[110,136],[136,162]]
  ,[[6,26],[26,54],[54,82],[82,110],[110,138],[138,166]]
  ,[[6,30],[30,58],[58,86],[86,114],[114,142],[142,170]]]


def index(chaine, niveau_correction, alignement):

  """
    cette methode permets d'extraire  
    les indices de la matrice qu'on peut remplir .


    Parametrs:

    chaine: c'est la chaine qu'on peut coder

    niveau_correction: c'est le niveau de correction soit L,Q,L,M


    alignement: c'est le centre du modéle d'alignement qu'on ne peut pas toucher
   """

  version=detrmine_version(chaine,niveau_correction)
  n=(((version-1)*4)+21)
  if version<7:
    liste=[]
    j=0
    while j<n:
        for i in range(n):
            if n-1-j>=0:
              liste.append([n-1-i,n-1-j])
            if n-2-j>=0:
              liste.append([n-1-i,n-2-j])
        if n-3-j==6:
          for i in range(n):
            if n-3-j>=0:
              liste.append([i,n-4-j])
            if n-4-j>=0:
              liste.append([i,n-5-j])
          break
        else:  
          for i in range(n):
            if n-3-j>=0:
              liste.append([i,n-3-j])
            if n-4-j>=0:
              liste.append([i,n-4-j])
        j=j+4
    for i in range(n):
      liste.append([n-1-i,3])
      liste.append([n-1-i,2])
    for i in range(n):
      liste.append([i,1])
      liste.append([i,0])
    
    ##supprimer les elemets principale
    rendononce=[]
    for i in range(9):
      for j in range(9):
        if not(j==6):
          liste.remove([i,j])
          if j==8 or i==8:
            rendononce.append([i,j])

    for i in range(9):
      for j in range(8):
        liste.remove([i,n-1-j])
        if i==8:
          rendononce.append([i,n-1-j])
          


    for i in range(8):
      for j in range(9):
        if not(j==6):
           liste.remove([n-1-i,j])
           if j==8:
              rendononce.append([n-1-i,j])
    
  
    for i in range(9,n-8):
      liste.remove([6,i])
      rendononce.append([6,i])
    rendononce.append([4*version+9,8])


    #Remarque tres important attention est que jusqu'a 
    for i in alignement:
      for k in range(5):
        for j in range(5):
          s=i[0] 
          z=i[1]
          if not [s-2+k,z-2+j] in rendononce:
            liste.remove([s-2+k,z-2+j])
  else:
    liste=[]
    j=0
    while j<n:
        for i in range(n):
            if n-1-j>=0:
              liste.append([n-1-i,n-1-j])
            if n-2-j>=0:
              liste.append([n-1-i,n-2-j])
        if n-3-j==6:
          for i in range(n):
            if n-3-j>=0:
              liste.append([i,n-4-j])
            if n-4-j>=0:
              liste.append([i,n-5-j])
          break
        else:  
          for i in range(n):
            if n-3-j>=0:
              liste.append([i,n-3-j])
            if n-4-j>=0:
              liste.append([i,n-4-j])
        j=j+4
    for i in range(n):
      liste.append([n-1-i,3])
      liste.append([n-1-i,2])
    for i in range(n):
      liste.append([i,1])
      liste.append([i,0])
    
    ##supprimer les elemets principale
    rendononce=[]
    for i in range(8):
      for j in range(8):
        if not(j==6):
          liste.remove([i,j])

    for i in range(8):
      for j in range(8):
        liste.remove([i,n-1-j])
    
          


    for i in range(8):
      for j in range(8):
        if not(j==6):
           liste.remove([n-1-i,j])
           
    
    for i in range(9,n-8):
      liste.remove([6,i])
      rendononce.append([6,i])
    
    for i in range(n-11,n-8):
      for j in range(6):
         rendononce.append([i,j])


    for i in range(6):
      for j in range(n-11,n-8):
         rendononce.append([i,j])
    rendononce.append([4*version+9,8])


    #Remarque tres important attention est que jusqu'a 
    for i in alignement:
      for k in range(5):
        for j in range(5):
          s=i[0] 
          z=i[1]
          if not [s-2+k,z-2+j] in rendononce:
            liste.remove([s-2+k,z-2+j])
  return liste

  
def Placement(chaine,niveau_correction):

  """
    cette methode permets de placer les pixels   
    danc la matrice .


    Parametrs:

    chaine: c'est la chaine qu'on peut coder

    niveau_correction: c'est le niveau de correction soit L,Q,L,M
   """
  version=detrmine_version(chaine,niveau_correction)
  n=(((version-1)*4)+21)

  #je déclare une matrice nulle
  m=[0 for i in range(n)] 
  m=[m for i in range(n)] 
  m=np.array(m)

  #Placement les modeles de recherches on note 1 pour les pixel en noir et 0 pour blanc 
  for i in range(7): 
    #haut a gauche
    m[0:1,0:i]=1 
    m[0:i,0:1]=1 
    m[6:7,0:i+1]=1
    m[0:i+1,6:7]=1
    #haut a droite
    m[0:1,n-7:n-i]=1 
    m[0:i,n-7:n-6]=1 
    m[6:7,n-7:n-i]=1
    m[0:i+1,n-1:n]=1
    #en bas a gauche
    m[n-7:n-6,0:i]=1 
    m[n-7:n-i,0:1]=1 
    m[n-1:n,0:i]=1
    m[n-i-1:n+1,6:7]=1
  m[2:5,2:5]=[[1,1,1],[1,1,1],[1,1,1]]
  m[n-5:n-2,2:5]=[[1,1,1],[1,1,1],[1,1,1]]
  m[2:5,n-5:n-2]=[[1,1,1],[1,1,1],[1,1,1]]
  #les séperateurs ils ont deja fait par definition du matrices

  #le module sombre et les zones réservées du version inferieure 7
  if version<7:
    for i in range(9):
      m[i:9,8:9]=9
      m[8:9,n-i:n+1]=9
      m[8:9,i:8]=9
      m[n-i+1:n+1,8:9]=9
    r = 8
    while r < n-8:
      m[r:n-8,6:7]=1
      m[r+1:n-8,6:7]=0
      m[6:7,r:n-8]=1
      m[6:7,r+1:n-8]=0
      r=r+2
  #le module sombre et les zones réservées du version supérieure 7
  else:
    m[n-11:n-8,0:6]=[[9,9,9,9,9,9],[9,9,9,9,9,9],[9,9,9,9,9,9]]
    m[0:6,n-11:n-8]=[[9,9,9],[9,9,9],[9,9,9],[9,9,9],[9,9,9],[9,9,9]]
  #les modéles de synchronisation
    r = 7
    while r < n-8:
      m[r:n-8,6:7]=1
      m[r+1:n-8,6:7]=0
      m[6:7,r:n-8]=1
      m[6:7,r+1:n-8]=0
      r=r+2

      
  #les motifs d'alignement
  matrice=[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]


  Centre=Alignement[version-1]
  alignement=[]
  for i in Centre: 
    #ici c'est grand probleme
    if (((0<=i[0]-2<=8) and (0<=i[1]-2<=8)) or ((n-8<= i[0]+3<=n-1) and (0<=i[1]-2<=8)) or((0<= i[0]-2<=8) and (n-8<=i[1]+3<=n-1))) ==False:


      s,z=i[0],i[1]
      m[s-2:s+3,z-2:z+3]=matrice



      alignement.append(i)
  m[4*version+9:4*version+9+1,8:9]=1
  
  """
  indexx=index(chaine,niveau_correction,alignement)
  j=2
  for i in indexx:
    m[i[0],i[1]]=j
    j=j+1
    if j==10:
      j=2
  m[6,7]=0
  m[7,6]=0
  """
  
  
  
  
  indexx=index(chaine,niveau_correction,alignement)
  data=[]
  for i in QR(chaine,niveau_correction):
    data.append(i)
  for i in indexx:
    m[i[0],i[1]]=int(data[0])
    del data[0]
  m[6,7]=0
  m[7,6]=0
  return m


