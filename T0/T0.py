import sys
import os
import glob
import codecs
import optparse
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt



def gerar_negativo(img):
	return 255 - img

def gerar_trns(img):
	return ((60/255) * img) + 120


def exibir_op(img, img_neg, img_tr):

	plt.subplot(2, 3, 1)
	plt.imshow(img, cmap="gray")
	plt.title('Imagem Original')

	plt.subplot(2, 3, 4)
	histogram_example = plt.hist(img)
	plt.title("Histograma da imagem Original")
	plt.xlabel("Níveis de cinza")
	plt.ylabel("Frequência")

	plt.subplot(2, 3, 2)
	plt.imshow(img_neg, cmap="gray")
	plt.title('Negativo da imagem')

	plt.subplot(2, 3, 3)
	plt.imshow(img_tr, cmap="gray", vmin=0, vmax=255)
	plt.title('Imagem Transformada')

	plt.show()

if __name__ == '__main__':

	img = misc.imread(sys.argv[1], mode="L")

	print("largura:",img.shape[1])
	print("altura:",img.shape[0])
	print("intensidade mínima:",img.min())
	print("intensidade máxima:",img.max())
	print("intensidade média: %0.f" % img.mean())

	img_neg = gerar_negativo(img)
	img_tr = gerar_trns(img)

	exibir_op(img,img_neg,img_tr)