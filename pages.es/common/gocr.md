# gocr

> Herramienta de reconocimiento óptico de caracteres.
> Reconoce caracteres utilizando su motor y solicita al usuario patrones desconocidos para almacenarlos en una base de datos.
> Más información: <https://manned.org/gocr.1>.

- Reconoce caracteres en una [i]magen y los escribe en un archiv[o]. Coloca la base de datos en una carpeta existente para que no se omita su uso. [m]odo 130 significa crear, usar y extender la base de datos:

`gocr -m 130 -p {{ruta/al/directorio_db}} -i {{ruta/a/imagen_entrada.png}} -o {{ruta/al/archivo_salida.txt}}`

- Reconoce caracteres y asume que todos son números:

`gocr -m 130 -p {{ruta/al/directorio_db}} -i {{ruta/a/imagen_entrada.png}} -o {{ruta/al/archivo_salida.txt}} -C "{{0..9}}"`

- Reconoce caracteres con certez[a] del 100% (los caracteres tienen una mayor probabilidad de ser tratados como desconocidos):

`gocr -m 130 -p {{ruta/al/directorio_db}} -i {{ruta/a/imagen_entrada.png}} -o {{ruta/al/archivo_salida.txt}} -a 100`
