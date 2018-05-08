import sys
import imageio
import matplotlib.pyplot as plt

#transforma a entrada em um array de bits 
def str2bin(entrada):
    return ''.join([bin(ord(i))[2:].zfill(8) for i in entrada])

#transforma a entrada binaria em charatere
def bin2str(n):
    n = int('0b'+n,2)
    return chr(n)

#recupera a msg que foi enviada transf o binario em chr e unindo
def txt_original(texto):
    return ''.join( [bin2str(texto[i:i+8]) for i in range(0,len(texto),8)])


#altera a camada especifica de bit
def alterar_bit(key, bit, alt):
    x = list(bin(key))
    x = x[::-1]
    x[bit] = alt
    return ''.join(x[::-1])

#funcao que insere o texto na imagem
def encode(img, msg, bit):
    bin_msg = str2bin(msg)
    
    dados = img.shape
    linhas = dados[0]
    colunas = dados[1]
    
    cont = 0
    for i in range(linhas):
        for j in range(colunas):
            for k in range(3):
                if(cont < len(bin_msg)):                                                
                    img[i,j,k] = int(alterar_bit(img[i,j,k], bit, bin_msg[cont]),2)                                        
                    cont += 1                    
    return img

if __name__ == '__main__':

	#Carregar a imagem com niveis de cinza
	
    img = imageio.imread(sys.argv[1])
    file = open(sys.argv[2], "r")
    str_text = file.read()
    img_code = encode(img, str_text, int(sys.argv[3]))
    imageio.imsave(sys.argv[4], img_code)
    file.close()