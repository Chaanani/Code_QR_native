
import math
from Module_Placement import *
from Penalty import *
from Chaine_version import *
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from Masquage import *


chaine="HELLO Word"
qrr=QRRRR(chaine,"H")
print("numbre of versin",detrmine_version(chaine,"H"))
matrice = cv.imread("Lena.png")  # charge le fichier dans une matrice de pixels couleur
plt.imshow(qrr,cmap='gray_r')   # affiche la matrice de triplets RVB
plt.show()