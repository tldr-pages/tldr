# pngtopam

> Convierte una imagen PNG a una imagen Netpbm.
> Vea también: `pamtopng`.
> Más información: <https://netpbm.sourceforge.net/doc/pngtopam.html>.

- Convierte la imagen PNG especificada en imagen Netpbm:

`pngtopam {{ruta/a/la/imagen.png}} > {{ruta/al/resultado.pam}}`

- Crea una imagen de salida que incluye tanto la imagen principal como la máscara de transparencia de la imagen de entrada:

`pngtopam -alphapam {{ruta/a/la/imagen.png}} > {{ruta/al/resultado.pam}}`

- Reemplaza píxeles transparentes por el color especificado:

`pngtopam {{[-m|-mix]}} {{[-ba|-background]}} {{color}} {{ruta/a/la/imagen.png}} > {{ruta/al/resultado.pam}}`

- Escribe los trozos de tEXt encontrados en la imagen de entrada al archivo de texto especificado:

`pngtopam {{[-te|-text]}} {{ruta/al/archivo.txt}} {{ruta/a/la/imagen.png}} > {{ruta/al/resultado.pam}}`
