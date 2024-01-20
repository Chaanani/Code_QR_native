import numpy as np
from Erreur_Correction_conding import *



def Interclater(x,y):


  """Cette methode permet
   de interclater les chaines

   paramerts:

   x: c'est le message
   y: la correction du message
  """
  x=np.array(x)
  y=np.array(y)
  chaine=''
  len_x=len(x[0])
  len_=len(y)
  
  if not(len_==0):
    len_y=len(y[0])
    if len_x<=len_y:
      for j in range(len_x):
        for i in x[:,j:j+1]:
          chaine=chaine+i[0]
        for i in y[:,j:j+1]:
          chaine=chaine+i[0]
      for j in range(len_x,len_y):
        for i in y[:,j:j+1]:
          chaine=chaine+i[0]
    else:
      for j in range(len_y):
        for i in x[:,j:j+1]:
          chaine=chaine+i[0]
        for i in y[:,j:j+1]:
          chaine=chaine+i[0]
      for j in range(len_y,len_x):
        for i in x[:,j:j+1]:
          chaine=chaine+i[0]
  else:

      for j in range(len_x):
        for i in x[:,j:j+1]:
          chaine=chaine+i[0]
  
  return chaine
"""data=detrmine_bloc("HELLO WORLD YOUNESS CHAANANI BORIS KHALID FERERE HFALI DHDGD HSYDD DHGDYD DHYDGTD GHYYF GHFY JHFTYTRTYUJKJ HHUIIH JUUYUU UUUUIUI","L")
chaine=Interclater(data[0],data[1])
j=0
for i in range(68):
   if not(chaine[j:j+8]==data[0][0][i]): 
     print("false")
   j=j+8
   if  not(chaine[j:j+8]==data[0][1][i]):
      print("false")
   j=j+8
print("ok")"""




def covert_binaire_correctio(chaine,niveau_correction):

   """
   Cette methode permet de convertir les correction
    des messages sous forme binaire

    parametrs:

    chaine: c'est la chaine qu'on peut coder

    niveau_correction: c'est le niveau de correction soit L,Q,L,M
   """

   x=Reed_Correction(chaine,niveau_correction)
   for i in range(len(x[0])):
     for j in range(len(x[0][i])):
        l=format(x[0][i][j],'b')
        x[0][i][j]=(8-len(l))*'0'+l
   if not(len(x[1])==0):
     for a in range(len(x[1])):
      for b in range(len(x[1][a])):
        q=format(x[1][a][b],'b')
        x[1][a][b]=(8-len(q))*'0'+q
   return x


def Interlacer_data_correction(chaine,niveau_correction):
   """
    cette methode fait l'interlacer entre les 
    messages et leurs corrections.


    Parametrs:

    chaine: c'est la chaine qu'on peut coder

    niveau_correction: c'est le niveau de correction soit L,Q,L,M
   """
   data=detrmine_bloc(chaine, niveau_correction)
   data_of_correction=covert_binaire_correctio(chaine,niveau_correction)
   return Interclater(data[0],data[1])+Interclater(data_of_correction[0],data_of_correction[1])







def Add_bits_reste(chaine,niveau_correction):
  """
    cette methode permets d'ajouter les zeros 
    apres  l'interlacer  .


    Parametrs:

    chaine: c'est la chaine qu'on peut coder

    niveau_correction: c'est le niveau de correction soit L,Q,L,M
   """
  version=detrmine_version(chaine,niveau_correction)
  bite_restent=[0,7,7,7,7,7,0,0,0,0,0,0,0,3,3,3,3,3,3,3,4,4,4,4,4,4,4,3,3,3,3,3,3,3,0,0,0,0,0,0]
  data=Interlacer_data_correction(chaine,niveau_correction)+bite_restent[version-1]*'0'
  return data

def QR(chaine,niveau_correction):
   """
   cette methode générer 
   le donnée final y a compris 
   les messages et leurs corrections:


   chaine: c'est la chaine qu'on peut coder

   niveau_correction: c'est le niveau de correction soit L,Q,L,M
   """
   return Add_bits_reste(chaine,niveau_correction)

