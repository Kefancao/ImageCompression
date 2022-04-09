# Image Compression with Discrete Cosine Transform

Similar to the Discrete Fourier Transform, the Discrete Cosine Transform (DCT) lends itself well to image compression. The jpeg standard employs DCT to perform image compression. 

Given, some tile size N and some compression tile size C. The compression ratio can be calculated by (N/C)^2 = R. It is the number of times an image has been compressed. Generally, as C approaches 0, the quality becomes worse. You may wonder why. This is because how image compression is done. For the python file attached with this repo, the algorithm works in the following way, 

- Convert the image into a matrix of rgb, grayscale, or rgba values
- For each N by N tile, perform a two dimensional DCT on the tile 
- Keep the top left C by C subtile of the N by N tile and store it in an matrix in an order-preserving way. 

That's it! This new matrix formed by all these C by C sub matrices is your compressed version of the image.

For an image of a tesla 🔥 

![tesla](https://user-images.githubusercontent.com/76069770/162551139-b2a9631c-7695-4480-aeb5-96d5bc3c743d.jpeg)

Compressed version looks like (4:1)

![tesla compressed](https://user-images.githubusercontent.com/76069770/162551148-f7c07a07-e3d1-4f35-8478-7c82df2e9067.png)

Decompressing, 
![00a8048e-eaa4-4b81-9725-e8367a092c51](https://user-images.githubusercontent.com/76069770/162551160-d250bd22-7ee9-46c7-b571-4bec3d49db3a.png)

Of course, it's easy to see there's some loss of quality, this is because we discarded a small part of the matrix, and it is reconstructed using the DCT.

Please feel free to play around with the script attached with this repo!

