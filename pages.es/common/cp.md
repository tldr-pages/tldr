# cp

> Copia archivos y directorios.

- Copia un archivo a otra ruta:

`cp {{ruta/hacia/archivo_original.ext}} {{ruta/hacia/archivo_copia.ext}}`

- Copia un archivo a un directorio, manteniendo el nombre del archivo:

`cp {{ruta/hacia/archivo_original.ext}} {{ruta/hacia/directorio_destino}}`

- Copia de forma recursiva un directorio y su contenido a otra ruta (si la ruta de destino existe, el directorio se copiará dentro):

`cp -R {{ruta/hacia/directorio_original}} {{ruta/hacia/directorio_copia}}`

- Copia de forma recursiva y verbosa un directorio (muestra un listado de los archivos copiados):

`cp -vR {{ruta/hacia/directorio_original}} {{ruta/hacia/directorio_copia}}`

- Copia archivos de texto a otra ruta de forma interactiva (pregunta al usuario antes de sobreescribir):

`cp -i {{*.txt}} {{ruta/hacia/directorio_destino}}`

- Copia enlaces simbólicos sin mantener la referencia al original:

`cp -L {{enlace}} {{ruta/hacia/directorio_destino}}`
