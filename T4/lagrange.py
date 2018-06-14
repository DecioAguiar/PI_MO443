from math import ceil, floor, pow
import numpy as np

def L(n,img,x_,y_,dx,dy):
    L1=L2=L3=L4=0
    if(not( floor(x_)-1 >= img.shape[1] or floor(y_)+n-2 >= img.shape[0] or floor(y_)+n-2 < 0 or  floor(x_)-1 < 0)):
        L1 = (-dx*(dx-1.)*(dx-2.)*img[floor(x_)-1,floor(y_)+n-2])/6 
    if(not( floor(x_)+1 >= img.shape[1] or floor(y_)+n-2 >= img.shape[0] or floor(y_)+n-2 < 0 or  floor(x_)+1 < 0)):
        L2 = (-dx*(dx+1.)*(dx-2.)*img[floor(x_)+1,floor(y_)+n-2])/2
    if(not( floor(x_) >= img.shape[1] or floor(y_)+n-2 >= img.shape[0] or floor(y_)+n-2 < 0 or  floor(x_) < 0)):
        L3 = ((dx+1)*(dx-1)*(dx-2)*img[floor(x_),floor(y_)+n-2])/2
    if(not( floor(x_)+2 >= img.shape[1] or floor(y_)+n-2 >= img.shape[0] or floor(y_)+n-2 < 0 or  floor(x_)+2 < 0)):
        L4 = (dx*(dx+1)*(dx-1)*img[floor(x_)+2,floor(y_)+n-2])/6

    return L1+L2+L3+L4

def lagrange(img, x_, y_):
    
    dx = x_ - floor(x_)
    dy = y_ - floor(y_)
    
    Ag = (-dy*(dy-1.)*(dy-2.)*L(1,img,x_,y_,dx,dy))/6
    Bg = ((dy + 1.)*(dy - 1.)*(dy - 2.)*L(2,img,x_,y_,dx,dy))/2
    Cg = (-dy*(dy+1.)*(dy-2.)*L(3,img,x_,y_,dx,dy))/2
    Dg = (dy*(dy+1.)*(dy-1.)*L(4,img,x_,y_,dx,dy))/6

    return abs(Ag+Bg+Cg+Dg)

def interpolacao(img, escala):
    nova_img = np.zeros((int(escala*(img.shape[0])),int(escala*(img.shape[1]))), np.uint8) 
    linhas = nova_img.shape[0]
    colunas = nova_img.shape[1]
    for l in range(linhas):
        for c in range(colunas):
            nova_img[l,c] = lagrange(img, (l/escala), (c/escala))
    return nova_img

def rotacao(img,theta):
    nova_img = np.zeros( ((img.shape[0]),(img.shape[1])), np.uint8) 
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
            nova_img[l,c] = lagrange(img,x_,y_)
    return nova_img

def escala(img, altura, largura):                   
    escala_altura = altura/img.shape[0] * 1.0
    escala_largura = largura/img.shape[1] * 1.0
    nova_img = np.zeros((int(escala_altura*(img.shape[0])),int(escala_largura*(img.shape[1]))), np.uint8) 
    linhas = nova_img.shape[0]
    colunas = nova_img.shape[1]
    for l in range(linhas):
        for c in range(colunas):
            nova_img[l,c] = lagrange(img,(l/escala_altura), (c/escala_largura))
    return nova_img                            
