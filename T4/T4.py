import cv2
import optparse
import numpy as np
from math import ceil, floor
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

def vizinho_mais_proximo(img,x_,y_):
    return img[round(x_), round(y_)]

def interpolacao_vmp(img, escala):
    nova_img = np.zeros((int(escala*(img.shape[0]-1)),int(escala*(img.shape[1]-1)))) 
    linhas = nova_img.shape[0]
    colunas = nova_img.shape[1]
    for l in range(linhas):
        for c in range(colunas):
            nova_img[l,c] = vizinho_mais_proximo(img,(l/escala), (c/escala))
    return nova_img

def bilinear(img,x_,y_):
    dx = x_ - floor(x_)
    dy = y_ - floor(y_)
    return (1-dx)*(1-dy)*img[floor(x_),floor(y_)] + dx*(1-dy)*img[floor(x_)+1, floor(y_)] + (1-dx)*dy*img[floor(x_), floor(y_)+1] + dx*dy*img[floor(x_)+1, floor(y_)+1]

def interpolacao_bilinear(img, escala):
    nova_img = np.zeros((int(escala*(img.shape[0]-1)),int(escala*(img.shape[1]-1)))) 
    linhas = nova_img.shape[0]
    colunas = nova_img.shape[1]
    for l in range(linhas):
        for c in range(colunas):
            nova_img[l,c] = bilinear(img, (l/escala), (c/escala))
    return nova_img

def P(t):
    if(t>0):
        return t
    else:
        return 0.0

def R(s):
    return (1/6.0) * ( (P(s+2) ** 3) - 4*(P(s+1)**3) + 6*(P(s+1)**3) - 4*(P(s-1)**3) )                        

def bicubica(img, x_, y_):
    dx = x_ - floor(x_)
    dy = y_ - floor(y_)
    soma = 0
    for m in range(-1,3,1):
        for n in range(-1,3,1):
            if( ((floor(x_) + m) >= 0) and ((floor(y_)+n) >= 0) and ( (floor(x_)+m) < img.shape[0] ) and ( (floor(y_) + n) < img.shape[1] )):                
                soma += (img[(floor(x_)+m), (floor(y_)+n)]) * R(m-dx) * R(dy-n)
    return soma                

def interpolacao_bicubica(img, escala):
    nova_img = np.zeros((int(escala*(img.shape[0]-1)),int(escala*(img.shape[1]-1)))) 
    linhas = nova_img.shape[0]
    colunas = nova_img.shape[1]
    for l in range(linhas):
        for c in range(colunas):
            nova_img[l,c] = bicubica(img, (l/escala), (c/escala))
    return nova_img



if __name__ == '__main__':
	main()