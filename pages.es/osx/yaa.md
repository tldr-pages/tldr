# yaa

> Crea y manipula archivos YAA.
> Más información: <https://keith.github.io/xcode-man-pages/yaa.1.html>.

- Crea un archivo a partir de un directorio:

`yaa archive -d {{ruta/al/directorio}} -o {{ruta/al/archivo_de_salida.yaa}}`

- Crea un archivo a partir de un fichero:

`yaa archive -i {{ruta/al/archivo}} -o {{ruta/al/archivo_de_salida.yaa}}`

- Extrae un archivo al directorio actual:

`yaa extract -i {{ruta/al/archivo.yaa}}`

- Lista el contenido de un archivo:

`yaa list -i {{ruta/al/archivo.yaa}}`

- Crea un archivo con un algoritmo de compresión específico:

`yaa archive -a {{algorithm}} -d {{ruta/al/directorio}} -o {{ruta/al/archivo_de_salida.yaa}}`

- Crea un archivo con un tamaño de bloque de 8 MB:

`yaa archive -b {{8m}} -d {{ruta/al/directorio}} -o {{ruta/al/archivo_de_salida.yaa}}`
