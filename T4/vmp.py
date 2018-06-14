from math import ceil, floor, pow
import numpy as np


def vizinho_mais_proximo(img,x_,y_):
    if(not( int(round(x_)) >= img.shape[1] or int(round(y_)) >= img.shape[0] or int(round(y_)) < 0 or  int(round(x_)) < 0)):
        return img[int(round(x_)), int(round(y_))]
    else: 
        return 0

def interpolacao(img, escala):
    nova_img = np.zeros((int(escala*(img.shape[0])),int(escala*(img.shape[1]))), np.uint8) 
    linhas = nova_img.shape[0]
    colunas = nova_img.shape[1]
    for l in range(linhas):
        for c in range(colunas):
            nova_img[l,c] = vizinho_mais_proximo(img,(l/escala), (c/escala))
    return nova_img

def rotacao(img, theta):
    nova_img = np.zeros( ((img.shape[0]),(img.shape[1])), np.uint8 ) 
    theta = np.deg2rad(theta)
    linhas = nova_img.shape[0]
    colunas = nova_img.shape[1]
    xm = linhas//2
    ym = colunas//2
    for l in range(linhas):
        for c in range(colunas):
            x_ = (l-xm)*np.cos(theta) + (c-ym)*np.sin(theta)
            x_ += xm
            y_ = (l-xm)*np.sin(theta) - (c-ym)*np.cos(theta)
            y_ += ym
            nova_img[l,c] = vizinho_mais_proximo(img,x_,y_)
    return nova_img

def escala(img, altura, largura):                   
    escala_altura = altura/img.shape[0] * 1.0
    escala_largura = largura/img.shape[1] * 1.0
    nova_img = np.zeros((int(escala_altura*(img.shape[0])),int(escala_largura*(img.shape[1]))), np.uint8) 
    linhas = nova_img.shape[0]
    colunas = nova_img.shape[1]
    for l in range(linhas):
        for c in range(colunas):
            nova_img[l,c] = vizinho_mais_proximo(img,(l/escala_altura), (c/escala_largura))
    return nova_img