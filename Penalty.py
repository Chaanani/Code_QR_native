


def cont_ligne_1(matrice):

  """
  cette methode qui calcule une partie de la penalité 1, 
  c'est le calcule des 1 successivement suivant les lignes

  parametrs:
  matrice: c'est la matrice qu'on peut calculer la penalité 1

  
  """
  n=matrice.shape[0]
  vercotr1=[1, 1, 1, 1, 1]
  score_penalty_1=0
  d=0
  for i in range(n):
    j=0
    r=0
    s=0
    while j<=n-5:
      if list(matrice[i,j:j+5])==vercotr1 :
        score_penalty_1=score_penalty_1+3
        for k in range(j+5,n,1):
           if matrice[i,k:k+1]==1:
              d=d+1
           else:
             r=k
             break 
             
      elif not(list(matrice[i,j:j+5])==vercotr1 ):
         s=5
         
      if s==5:
        j=j+1
      elif r==0:
        j=n-4
      else:
        j=r+1 
      r=0
      s=0     
  return d+score_penalty_1



def cont_colone_1(matrice):
  """
  cette methode qui calcule une partie de la penalité 1, 
  c'est le calcule des 1 successivement suivant les colonnes

  parametrs:
  matrice: c'est la matrice qu'on peut calculer la penalité 1"""

  n=matrice.shape[1]
  vercotr1=[1, 1, 1, 1, 1]
  score_penalty_1=0
  d=0
  for j in range(n):
    i=0
    r=0
    s=0
    while i<=n-5:
      if list(matrice[j:j+5,i])==vercotr1 :
        score_penalty_1=score_penalty_1+3
        for k in range(i+5,n,1):
           if matrice[k:k+1,j]==1:
              d=d+1
           else:
             r=k
             break 
             
      elif not(list(matrice[j:j+5,i])==vercotr1 ):
         s=5
         
      if s==5:
        i=i+1
      elif r==0:
        i=n-4
      else:
        i=r+1 
      r=0
      s=0     
  return d+score_penalty_1


  
def cont_colone_0(matrice):

  """
  cette methode qui calcule une partie de la penalité 1, 
  c'est le calcule des 0 successivement suivant les colonnes

  parametrs:
  matrice: c'est la matrice qu'on peut calculer la penalité 1"""
  n=matrice.shape[1]
  vercotr0=[0, 0, 0, 0, 0]
  score_penalty_1=0
  d=0
  for j in range(n):
    i=0
    r=0
    s=0
    while i<=n-5:
      if list(matrice[j:j+5,i])==vercotr0 :
        score_penalty_1=score_penalty_1+3
        for k in range(i+5,n,1):
           if matrice[k:k+1,j]==0:
              d=d+1
           else:
             r=k
             break 
             
      elif not(list(matrice[j:j+5,i])==vercotr0 ):
         s=5
         
      if s==5:
        i=i+1
      elif r==0:
        i=n-4
      else:
        i=r+1 
      r=0
      s=0 
  return d+score_penalty_1




def cont_ligne_0(matrice):
  """
  cette methode qui calcule une partie de la penalité 1, 
  c'est le calcule des 0 successivement suivant les lignes

  parametrs:
  matrice: c'est la matrice qu'on peut calculer la penalité 1"""
  n=matrice.shape[0]
  vercotr0=[0, 0, 0, 0, 0]
  score_penalty_1=0
  d=0
  for i in range(n):
    j=0
    r=0
    s=0
    while j<=n-5:
      if list(matrice[i,j:j+5])==vercotr0 :
        score_penalty_1=score_penalty_1+3
        for k in range(j+5,n,1):
           if matrice[i,k:k+1]==0:
              d=d+1
           else:
             r=k
             break 
             
      elif not(list(matrice[i,j:j+5])==vercotr0):
         s=5
         
      if s==5:
        j=j+1
      elif r==0:
        j=n-4
      else:
        j=r+1 
      r=0
      s=0       
  return d+score_penalty_1



def penalty1(matrice):

  """
  cette methode  calcule la penalité 1 
  
  parametrs:
  matrice: c'est la matrice qu'on peut calculer la penalité 1"""
  return cont_ligne_1(matrice)+cont_ligne_0(matrice)+cont_colone_1(matrice)+cont_colone_0(matrice)



def penalty2(matrice):
  """
  cette methode  calcule la penalité 2
  
  parametrs:
  matrice: c'est la matrice qu'on peut calculer la penalité 2"""
  n=matrice.shape[0]
  s=0
  for i in range(n-1):
    for j in range(n-1):
      if matrice[i,j:j+1]==0 and matrice[i+1,j:j+1]==0  and matrice[i,j+1:j+2]==0 and matrice[i+1,j+1:j+2]==0:
        s=s+1
      elif  matrice[i,j:j+1]==1 and matrice[i+1,j:j+1]==1  and matrice[i,j+1:j+2]==1 and matrice[i+1,j+1:j+2]==1:
        s=s+1
  return 3*s



def penalty3(matrice):
  """
  cette methode  calcule la penalité 3
  
  parametrs:
  matrice: c'est la matrice qu'on peut calculer la penalité 3"""
  n=matrice.shape[0]
  s=0
  for i in range(n):
    for j in range(n):
      if list(matrice[i,j:j+11])==[1,0,1,1,1,0,1,0,0,0] or list(matrice[i,j:j+11])==[0,0,0,1,0,1,1,1,0,1]:
        s=s+40
  for j in range(n):
    for i in range(n):
      if list(matrice[i:i+11,j])==[1,0,1,1,1,0,1,0,0,0] or list(matrice[i:i+11,j])==[0,0,0,1,0,1,1,1,0,1]:
        s=s+40
  return s



def penalty4(matrice):

  """
  cette methode  calcule la penalité 4 
  
  parametrs:
  matrice: c'est la matrice qu'on peut calculer la penalité 4"""
  n=matrice.shape[0]
  s=0
  for i in range(n):
    for j in range(n):
      if matrice[i,j]==1:
        s=s+1
  taille=n*n
  persontage=(s/taille)*100 
  qot=persontage/5
  multip_inf=int(qot)*5
  multip_sup=multip_inf+5
  abs_multi_inf=abs(multip_inf-50)/5
  abs_multi_sup=abs(multip_sup-50)/5
  if abs_multi_inf>abs_multi_sup:
    resultat=abs_multi_sup*10
  else:
    resultat=abs_multi_inf*10
  return resultat


def total_penalty(matrice):
  """
  cette methode  calcule la somme des  penalités 
  
  parametrs:
  matrice: c'est la matrice qu'on peut calculer la somme des penalités"""

  return penalty1(matrice)+penalty2(matrice)+penalty3(matrice)+penalty4(matrice)