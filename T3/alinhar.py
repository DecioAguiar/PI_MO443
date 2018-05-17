import matplotlib.pyplot as plt
from skimage.transform import rotate
from skimage.transform import hough_line, hough_line_peaks
from skimage import feature
import numpy as np
import math as mt
from scipy import misc
import sys

def objetivo(img,theta):
    img_rot = rotate(img,theta)
    hist_rot = np.sum(img_rot, axis=-1)
    soma = 0
    for i in range(len(hist_rot)-1):
        soma += (hist_rot[i] - hist_rot[i+1])**2
    return soma

def proj_horizontal(img):
    img_canny = feature.canny(img, sigma=3)
    valor = []
    for theta in range(-90, 90, 1):
        valor.append((objetivo(img_canny, theta), theta))
    return max(valor)[1]

def retorna_coluna(out):
    maior_coluna = 0
    maior = out[0,0]
    for l in range(out.shape[0]):
        for c in range(out.shape[1]):        
            if maior < out[l,c]:
                maior = out[l,c]
                maior_coluna = c
    return maior_coluna

def hough_angle(img):
    img = 255 - img
    img_canny = feature.canny(img, sigma=3)
    out, angles, d = hough_line(img_canny)
    coluna = retorna_coluna(out)
    angulo = angles[coluna]
    angulo = np.rad2deg(angulo)
    if angulo < 0:
        return angulo + 90
    else: 
        return angulo - 90

if __name__ == '__main__':
	#Carregar a imagem com niveis de cinza
	img = misc.imread(sys.argv[1], mode='L')    
	plt.imshow(img, cmap="gray")
	plt.show()
	#modo a ser usado
	modo = int(sys.argv[2])
	#salvar saida
	saida = sys.argv[3]
	if(modo):
		angulo = int(proj_horizontal(img))
		print(angulo)
		img_rot = rotate(img, angulo, order=3, mode="edge")
		plt.imshow(img_rot, cmap="gray")
		misc.imsave(saida, img_rot)
		plt.show()
	else:
		angulo = int(hough_angle(img))
		print(angulo)
		img_rot = rotate(img, angulo, order=3, mode="edge")
		plt.imshow(img_rot, cmap="gray")
		misc.imsave(saida, img_rot)
		plt.show()