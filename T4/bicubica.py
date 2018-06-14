from math import ceil, floor, pow
import numpy as np

def P(t):
    if(t>0.):
        return t
    else:
        return 0.0

def R(s):
    return 1/6*(pow(P(s+2),3) - 4*pow(P(s+1),3) + 6*pow(P(s),3) - 4*pow(P(s-1),3))

def bicubica(img, x_, y_):
    dx = x_ - floor(x_)
    dy = y_ - floor(y_)
    soma = 0
    for m in range(-1,2):
        for n in range(-1,2):
            if( ((floor(x_) + m) >= 0) and ((floor(y_)+n) >= 0) and ( (floor(x_)+m) < img.shape[0] ) and ( (floor(y_) + n) < img.shape[1] )):                
                soma += (img[(floor(x_)+m), (floor(y_)+n)]) * R(m-dx) * R(dy-n)
    return int(soma)

def interpolacao(img, escala):
    nova_img = np.zeros((int(escala*(img.shape[0])),int(escala*(img.shape[1]))), np.uint8) 
    linhas = nova_img.shape[0]
    colunas = nova_img.shape[1]
    for l in range(linhas):
        for c in range(colunas):
            nova_img[l,c] = bicubica(img, (l/escala), (c/escala))
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
            nova_img[l,c] = bicubica(img,x_,y_)
    return nova_img

def escala(img, altura, largura):                   
    escala_altura = altura/img.shape[0] * 1.0
    escala_largura = largura/img.shape[1] * 1.0
    nova_img = np.zeros((int(escala_altura*(img.shape[0])),int(escala_largura*(img.shape[1]))), np.uint8) 
    linhas = nova_img.shape[0]
    colunas = nova_img.shape[1]
    for l in range(linhas):
        for c in range(colunas):
            nova_img[l,c] = bicubica(img,(l/escala_altura), (c/escala_largura))
    return nova_img            