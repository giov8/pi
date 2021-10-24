# Giovani G Marciniak
# GRR20182921
# Modificado em 23/10/2021

import cv2
import numpy as np
import random
import sys

# Função que cria imagem ruidosa
def sp_noise(image,prob):
        
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

# Chega se parametros da linha de comando estão corretos
if len(sys.argv) != 5:
    raise ValueError('USO DO PROGRAMA: "python3 filtro.py <imagem original> <nível de ruído> <filtro>  <nome da imagem de saída>"')

# Trata linha de comando
img_path = sys.argv[1]
noise_level = float(sys.argv[2])
filter = sys.argv[3]
img_path_out = sys.argv[4]

# Abre a imagem
img = cv2.imread(img_path)

# Cria imagem ruidoza
img_noisy = sp_noise(img, noise_level)

# Salva imagem ruidoza
# cv2.imwrite("noisy.png",img_noisy)

# Faz tratamento correspondente ao filtro requisitado:
if (filter == '0'):
    print("Filtro selecionado: Media")
    img_out = cv2.blur(img_noisy,(5,5))
    print("PSNR Ruidoso: ", cv2.PSNR(img,img_noisy))
    print("PSNR: ", cv2.PSNR(img,img_out))

if (filter == '1'):
    print("Filtro selecionado: Mediana")
    img_out = cv2.medianBlur(img_noisy,3)
    print("PSNR Ruidoso: ", cv2.PSNR(img,img_noisy))
    print("PSNR: ", cv2.PSNR(img,img_out))
    

if (filter == '2'):
    print("Filtro selecionado: Empilhamento")
    noisy_list = []
    noisy_len = 20
    for x in range(noisy_len):                                  # cria 'noisy_len' imagens com ruido
        img_noisy = sp_noise(img, noise_level)
        noisy_list.append(img_noisy)
    
    sum = np.zeros(img.shape)
    for i in noisy_list:                                        # soma todas as imagens criadas
        sum = sum + i                               
    img_out = (sum//len(noisy_list)).astype(np.uint8)           # Converte para a mesma unidade de imagens opencv
    
    print("PSNR: ", cv2.PSNR(img,img_out))

if (filter == '3'): 
    print("Filtro selecionado: Gaussianol")
    img_out = cv2.GaussianBlur(img,(9,9),0)
    print("PSNR Ruidoso: ", cv2.PSNR(img,img_noisy))
    print("PSNR: ", cv2.PSNR(img,img_out))
    

# Salva imagem
cv2.imwrite(img_path_out,img_out)

# Salva comparação
#comp = np.concatenate((img_noisy, img_out), axis=1)
#cv2.imwrite("comparison-gau.png",comp)
