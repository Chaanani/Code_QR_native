from operator import xor


def delet_zeros(resultat):

  """
  cette methode fait la supprresion des premiers  zeros du resultat


  parametrs:
  resultat: chaine qu'on peut supprimer les premiers zeros 
  """
  x=[]
  for i in resultat:
    x.append(i)
  for i in resultat:
    if int(i)==0:
      del x[0]
    else:
      break
  resultat=''
  for i in x:
      resultat=resultat+i
  return resultat

def devision_binary(chaine_bits):

    """
  cette methode fait la division eucludienne entre le varaible "chaine_bits" et '10100110111'


  parametrs:

  chaine_bits: c'est la chaine sur laquelle on fait la division par '10100110111'

  
  """

    poly_generat='10100110111'
    resultat=chaine_bits+10*'0'
    resultat=delet_zeros(resultat)
    while len(resultat)>=11:
      r=len(resultat)-len(poly_generat)
      poly_generatt=poly_generat+r*'0'
      resultat=format(xor(int(resultat,2),int(poly_generatt,2)),'b')
      resultat=delet_zeros(resultat)
    resultat=(10-len(resultat))*'0'+resultat
    resultat=chaine_bits+resultat
    resultat=format(xor(int(resultat,2),int('101010000010010',2)),'b')
    long=15-len(resultat)
    resultat=long*'0'+resultat
    return resultat
    
def chaine_format_7(version):

  """
  cette methode génére chaine de version qui superieur ou egale 7


  parametrs:

  version: c'est la la version du code QR

  """
  poly_generat='1111100100101'
  chaine_bits=format(version,'b')
  chaine_bits=(6-len(chaine_bits))*'0'+chaine_bits
  resultat=chaine_bits+(18-len(chaine_bits))*'0'
  resultat=delet_zeros(resultat)

  while len(resultat)>12:
    r=len(resultat)-len(poly_generat)
    poly_generatt=poly_generat+r*'0'
    resultat=format(xor(int(resultat,2),int(poly_generatt,2)),'b')
  resultat=(12-len(resultat))*'0'+resultat
  resultat=chaine_bits+resultat
  resultat=(18-len(resultat))*'0'+resultat
  return resultat


def chaine_format_6(n_correction,nbre_masque):

  """
  cette methode génére chaine de version qui inferieur 7


  parametrs:

  n_correction: c'est le niveau de correction

  nbre_masque: c'est le nombre de masque
  """
  boris=format(nbre_masque,'b')
  if n_correction=="L":
    chaine_bits='01'+(3-len(boris))*'0'+boris
    resultat=devision_binary(chaine_bits)
  elif n_correction=="M":
    chaine_bits='00'+(3-len(boris))*'0'+boris
    resultat=devision_binary(chaine_bits)
  elif n_correction=="Q":
    chaine_bits='11'+(3-len(boris))*'0'+boris
    resultat=devision_binary(chaine_bits)
  elif n_correction=="H":
    chaine_bits='10'+(3-len(boris))*'0'+boris
    resultat=devision_binary(chaine_bits)
  return resultat
  

