from scipy.fftpack import dct, idct
from matplotlib import pyplot as plt
import numpy as np

def Show(g, title=''):
    '''
     Show(g, title='')
     
     Displays the image g as a graylevel image with intensities
     clipped to the range [0,255].
    '''
    plt.imshow(np.clip(g, a_min=0, a_max=255)/255., cmap='gray');
    plt.axis('off');
    plt.title(title);
    
def myJPEGCompress(f, T, D):
   '''
   G = myJPEGCompress(f, T, D)
   
   Input
      f is the input image, a 2D array of real numbers
      T is the tile size to break the input image into
      D is the size of the block of Fourier coefficients to keep
         (Bigger values of D result in less loss, but less compression)
   
   Output
      G is the compressed encoding of the image
   
   Example: If f is 120x120, then
   
      G = myJPEGCompress(f, 10, 4)
   
   would return an array (G) of size 48x48.
   '''
   
   h,w = np.shape(f)  # returns the width and height of f
   G = np.zeros( (int(np.floor(h/T)*D), int(np.floor(w/T)*D)) )
   for i in range(h//T):
      for j in range(w//T):
         # Extract the T x T tiles
         T_subarr = np.zeros((T, T))
         for y in range(T):
            for x in range(T):
               T_subarr[y][x] = f[y + i * T][x + j * T]
         
         # Perform DCT on the tiles
         T_subarr = dct(dct(T_subarr, type=1, norm='forward', axis=0), type=1, norm='forward', axis=1)
         # Extract the D x D block of coefficients
         for row in range(D):
            for col in range(D):
               G[row + i * D][col + j * D] = T_subarr[row][col]



   return G

def myJPEGDecompress(G, T, D):
   '''
   f = myJPEGDecompress(G, T, D)
   
   Input
      G is the compressed encoding, a 2D array of real numbers
      T is the tile size for reassembling the decompressed image
      D is the size of the blocks of Fourier coefficients that were
         kept when the image was compressed
         (Bigger values of D result in less loss, but less compression)
   
   Output
      f is the decompressed, reconstructed image
   
   Example: If G is 48x48, then
   
      f = myJPEGDecompress(G, 10, 4);
   
   would return an array (f) of size 120x120.
   '''
   n_hblocks = int( np.shape(G)[0]/D)
   n_wblocks = int( np.shape(G)[1]/D)
   
   f = np.zeros( (T*n_hblocks, T*n_wblocks) )

    # ==== YOUR CODE HERE ====
   for i in range(n_hblocks):
      for j in range(n_wblocks):
         # Extract the D x D block of coefficients onto a T x T array
         T_subarr = np.zeros((T, T))
         for row in range(D):
            for col in range(D):
               T_subarr[row][col] = G[row + i * D][col + j * D]

         # Perform 2D-IDCT
         T_subarr = idct(idct(T_subarr, axis=0, norm='backward', type=1), type=1, norm ='backward', axis=1)
         # Insert the T x T block of coefficients into the output array
         for y in range(T):
            for x in range(T):
               f[y + i * T][x + j * T] = T_subarr[y][x]

   return f


# Feel free to replace this name line with any image file you'd like!
name = 'tesla.jpeg'
f = plt.imread(name)[:,:,0]
print(f'Original has shape: {np.shape(f)}')

# Function to demonstrate compression/decompression 
def demonstrateJPEGCompression(f, T, D):
	f_comp = myJPEGCompress(f, T, D)
	ratio = NumPixels(f)/NumPixels(f_comp)
	print(f"Compressed shape: {np.shape(f_comp)}, with ratio: {ratio}")
	plt.figure(figsize=[10,10]); Show(f_comp, f"{int(ratio)}:1 Ratio Compression")
	f_decomp = myJPEGDecompress(f_comp, T, D)
	plt.figure(figsize=[10,10]); Show(f_decomp, f"{int(ratio)}:1 Decompressed")

# 4:1
demonstrateJPEGCompression(f, 20, 10)
# 25:1
demonstrateJPEGCompression(f, 20, 4)
# 100:1
demonstrateJPEGCompression(f, 20, 2)
