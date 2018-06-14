from math import ceil, floor, pow
import numpy as np

def bilinear(img,x_,y_):
    dx = x_ - floor(x_)
    dy = y_ - floor(y_)
    
    v1=v2=v3=v4=0
    
    if(not( floor(x_) >= img.shape[1] or floor(y_) >= img.shape[0] or floor(y_) < 0 or  floor(x_) < 0)):
        v1 = img[floor(x_),floor(y_)]
    if(not( floor(x_)+1 >= img.shape[1] or floor(y_) >= img.shape[0] or floor(y_) < 0 or  floor(x_)+1 < 0)):
        v2 = img[floor(x_)+1, floor(y_)]
    if(not( floor(x_) >= img.shape[1] or floor(y_)+1 >= img.shape[0] or floor(y_)+1 < 0 or  floor(x_) < 0)):
        v3 = img[floor(x_), floor(y_)+1]
    if(not( floor(x_)+1 >= img.shape[1] or floor(y_)+1 >= img.shape[0] or floor(y_)+1 < 0 or  floor(x_)+1 < 0)):
        v4 = img[floor(x_)+1, floor(y_)+1]
    
    return (1-dx)*(1-dy)*v1 + dx*(1-dy)*v2 + (1-dx)*dy*v3 + dx*dy*v4

def interpolacao(img, escala):
    nova_img = np.zeros((int(escala*(img.shape[0])),int(escala*(img.shape[1]))), np.uint8) 
    linhas = nova_img.shape[0]
    colunas = nova_img.shape[1]
    for l in range(linhas):
        for c in range(colunas):
            nova_img[l,c] = bilinear(img, (l/escala), (c/escala))
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
            nova_img[l,c] = bilinear(img,x_,y_)
    return nova_img

def escala(img, altura, largura):                   
    escala_altura = altura/img.shape[0] * 1.0
    escala_largura = largura/img.shape[1] * 1.0
    nova_img = np.zeros((int(escala_altura*(img.shape[0])),int(escala_largura*(img.shape[1]))), np.uint8) 
    linhas = nova_img.shape[0]
    colunas = nova_img.shape[1]
    for l in range(linhas):
        for c in range(colunas):
            nova_img[l,c] = bilinear(img,(l/escala_altura), (c/escala_largura))
    return nova_img