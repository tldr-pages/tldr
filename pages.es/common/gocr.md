# gocr

> Herramienta de reconocimiento óptico de caracteres.
> Reconoce caracteres utilizando su motor y solicita al usuario patrones desconocidos para almacenarlos en una base de datos.
> Más información: <https://manned.org/gocr.1>.

- Reconoce caracteres en la imagen de entrada [i]nput y su salida [o]utput en el archivo dado. Coloca la base de datos ([p]) en `ruta/al/directorio_db` (verifica que la carpeta existe o se omitirá silenciosamente el uso de la base de datos). [m]odo 130 significa crear + usar + extender base de datos:

`gocr -m 130 -p {{ruta/al/directorio_db}} -i {{ruta/a/imagen_entrada.png}} -o {{ruta/al/archivo_salida.txt}}`

- Reconoce caracteres y asume que todos los [C]aracteres son números:

`gocr -m 130 -p {{ruta/al/directorio_db}} -i {{ruta/a/imagen_entrada.png}} -o {{ruta/al/archivo_salida.txt}} -C "{{0..9}}"`

- Reconoce caracteres con una certez[a] del 100% (los caracteres tienen una mayor probabilidad de ser tratados como desconocidos):

`gocr -m 130 -p {{ruta/al/directorio_db}} -i {{ruta/a/imagen_entrada.png}} -o {{ruta/al/archivo_salida.txt}} -a 100`
