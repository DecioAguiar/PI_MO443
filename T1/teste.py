import matplotlib
import matplotlib.pyplot as plt

from scipy import misc
from skimage.filters import try_all_threshold

img = misc.imread("objetos1.png", mode="L")

fig, ax = try_all_threshold(img, verbose=False)
plt.show()