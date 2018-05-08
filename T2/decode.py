import sys
import imageio
import matplotlib.pyplot as plt
import numpy as np

def str2bin(entrada):
    return ''.join([bin(ord(i))[2:].zfill(8) for i in entrada])

def recuperar_bit(key, bit):
    x = list(bin(key)[2:].zfill(8))
    x = x[::-1]
    return x[bit]

def bin2str(n):
    n = int('0b'+n,2)
    return chr(n)

def txt_original(texto):
    return ''.join( [bin2str(texto[i:i+8]) for i in range(0,len(texto),8)])

def decode(img, bit):
    
    dados = img.shape
    linhas = dados[0]
    colunas = dados[1]
    
    texto = ""
    texto_original = ""
    cont = 0
    for i in range(linhas):
        for j in range(colunas):
            for k in range(3):                                           
                texto = texto + recuperar_bit(img[i,j,k], bit)                                                                   
    return txt_original(texto)

def showPlaneBit(image):

    ims = np.mod(np.floor(image/1), 2)
    plt.imshow(ims)
    misc.imsave("ims0.png", ims)
    plt.show()

    ims = np.mod(np.floor(image/2), 2)
    plt.imshow(ims)
    misc.imsave("ims1.png", ims)
    plt.show()

    ims = np.mod(np.floor(image/4), 2)
    plt.imshow(ims)
    misc.imsave("ims2.png", ims)

    plt.show()

    ims = np.mod(np.floor(image/128), 2)
    plt.imshow(ims)
    misc.imsave("ims3.png", ims)
    plt.show()
    return

if __name__ == '__main__':

    #Carregar a imagem com niveis de cinza
    img = imageio.imread(sys.argv[1])    
    str_write = decode(img, int(sys.argv[2]))
    file = open("saida.txt", "w")
    file.write(str_write)
    file.close()
