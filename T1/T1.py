#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
from scipy import misc
from skimage import measure
from skimage.color import rgb2gray
from skimage.filters import threshold_mean
import matplotlib.pyplot as plt

def exibir_entrada(img, img_col):
	plt.subplot(1, 2, 1)
	plt.imshow(img_col, cmap="gray")
	plt.title('Imagem Original')

	plt.subplot(1, 2, 2)
	plt.imshow(img, cmap="gray")
	plt.title('Imagem em niveis de cinza')

def mostrar_contorno(img):
	#Achar o contorno dos objetos da imagem
	contours = measure.find_contours(img, 0.8)
	
	#Mostrar o contorno dos objetos obtidos em fundo branco
	nova_img = np.ones(img.shape) * 255
	
	fig, ax = plt.subplots()
	ax.imshow(nova_img, cmap=plt.cm.gray, vmin=0, vmax=255)

	for n, contour in enumerate(contours):
	    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

	ax.axis('image')
	plt.title('Contorno dos objetos')
	plt.show()

def mostrar_enumeracao(img, props):
	contours = measure.find_contours(img, 0.8)
	nova_img = np.ones(img.shape) * 255
	#Enumerar as regioes encontradas
	fig, ax = plt.subplots()
	ax.imshow(nova_img, cmap=plt.cm.gray, vmin=0, vmax=255)

	for n, contour in enumerate(contours):
	    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

	ax.axis('image')
	for i in range(1,len(props)): 
	    plt.text( int(props[i].centroid[1]-6),int(props[i].centroid[0]+4), "%d" % i)
	plt.title('Objetos enumerados')
	plt.show()

def gerar_hist(props):
	area = []
	for i in range(1,len(props)):
	    area.append(props[i].area)

	plt.hist(area,bins=3, facecolor='b', normed=False)
	plt.autoscale(enable=True, axis='y', tight=False)
	plt.title("Histograma de áreas dos objetos")
	plt.xlabel("Área")
	plt.ylabel("Número de objetos")
	plt.show()

def exibe_info(props):
	#Exibe info dos objetos da imagem
	print("Número de regiões: %d" % (len(props)-1))
	for i in range(1,len(props)):
		print("região: %d perimetro: %d área: %d" % (i,props[i].perimeter,props[i].area))

	grande = 0
	pequena = 0
	media = 0
	for i in range(1,len(props)):
	    if (props[i].area >= 3000):
	        grande +=1
	    elif (props[i].area >= 1500):
	        media +=1
	    else:
	        pequena +=1

	print("número de regioes pequenas: %d" % pequena)
	print("número de regioes médias: %d" % media)
	print("número de regioes grandes: %d" % grande)


if __name__ == '__main__':

	#Carregar a imagem com niveis de cinza
	img_col = misc.imread(sys.argv[1])
	img = misc.imread(sys.argv[1], mode="L")

	exibir_entrada(img, img_col)

	mostrar_contorno(img)

	#Gerar o rotulo dos objetos e os atributos de cada regiao
	label_obj = measure.label(img, neighbors=4, connectivity=img.ndim, background=None)
	label_obj = measure.label(img)
	props = measure.regionprops(label_obj)

	mostrar_enumeracao(img,props)

	exibe_info(props)

	gerar_hist(props)