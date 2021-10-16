# Giovani G Marciniak
# GRR20182921
# Modificado em 15/10/2021

import cv2
import numpy as np
import sys

# Chega se parametros da linha de comando estão corretos
if len(sys.argv) != 3:
    raise ValueError('USO DO PROGRAMA: "python3 banana.py img1.png out.png"')

# Trata linha de comando
img_path = sys.argv[1]
img_path_out = sys.argv[2]

# Abre a imagem
img = cv2.imread(img_path)

# Normaliza a imagem
resultimage = np.zeros((800, 800))
img_normalized = cv2.normalize(img,resultimage, 0, 100, cv2.NORM_MINMAX)

# Salva imagem normalizada
#cv2.imwrite('NORM_'+img_path,normalizedimage)

# Convete para HSV
#img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)                  # Imagem sem normalizar (resultado pior)
img_hsv = cv2.cvtColor(img_normalized, cv2.COLOR_BGR2HSV)

# Aplica filtro de desfoque para facilitar encontrar as cores e remover pontos
img_blured = cv2.medianBlur(img_hsv ,7)

# Define valores superiores e inferiores para a gama
lower = np.array([17, 64, 67])
upper = np.array([28, 226, 127])

# Define a máscara a partir das cores dos limites inferiores e superiores
mask = cv2.inRange(img_blured, lower, upper)

# Aplica máscara a imagem
masked_img = cv2.bitwise_and(img, img, mask= mask)

# Salva imagem
cv2.imwrite(img_path_out,masked_img)