import numpy as np
from math import ceil, floor, pow
import matplotlib.pyplot as plt
import imageio
import optparse
import vmp
import lagrange
import bicubica
import bilinear

#Vetor contendo os objetos de modo de interpolacao
interpolacoes = [vmp, bilinear, bicubica, lagrange]

def main():

	parser = optparse.OptionParser()
	parser.add_option('-a', '--angle', type='float', dest='angle', default=None, help='angulo de rotação medido em graus no sentido anti-horário')
	parser.add_option('-e', '--scale', type='float', dest='scale', default=None, help='fator de escala')
	parser.add_option('-d', '--dimension', type='int', dest='dimension', default=None, help='dimensão da imagem de saída em pixels', nargs=2)
	parser.add_option('-i', '--input', type='string', dest='input', default=None, help='caminho da imagem de entrada')
	parser.add_option('-o', '--output', type='string', dest='output', default="out.png", help='caminho da imagem de entrada')
	parser.add_option('-m', '--mode', type='choice', choices=['0','1','2','3'], dest='mode', default=0, help='interpolacao a ser usada')
	(options, args) = parser.parse_args()

	img = imageio.imread(options.input)

	if(options.angle != None):
		saida = interpolacoes[int(options.mode)].rotacao(img, options.angle)		
	elif(options.scale != None):
		saida = interpolacoes[int(options.mode)].interpolacao(img, options.scale)
	elif(options.dimension != None):
		saida = interpolacoes[int(options.mode)].escala(img, options.dimension[0], options.dimension[1])

	imageio.imsave(options.output, saida)

	plt.imshow(img, cmap="gray")
	plt.title("Imagem de Entrada")
	plt.show()
	plt.imshow(saida, cmap="gray")
	plt.title("Imagem de Saida")
	plt.show()

if __name__ == '__main__':
	main()
