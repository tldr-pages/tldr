# cp

> Copia archivos y directorios.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>.

- Copia un archivo a otra ubicación:

`cp {{ruta/al/archivo_de_origen.ext}} {{ruta/al/archivo_destino.ext}}`

- Copia un archivo en otro directorio, manteniendo el nombre del archivo:

`cp {{ruta/al/archivo_de_origen.ext}} {{ruta/al/directorio_destino}}`

- Copia recursivamente el contenido de un directorio a otra ubicación (si el destino existe, el directorio se copia dentro de él):

`cp {{[-r|--recursive]}} {{ruta/al/directorio_de_origen}} {{ruta/al/directorio_de_destino}}`

- Copia un directorio de forma recursiva, en modo detallado (muestra los archivos a medida que se copian):

`cp {{[-vr|--verbose --recursive]}} {{ruta/al/directorio_de_origen}} {{ruta/al/directorio_de_destino}}`

- Copia varios archivos a la vez en un directorio:

`cp {{[-t|--target-directory]}} {{ruta/al/directorio_de_destino}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Copia archivos de texto a otra ubicación, en modo interactivo (pregunta al usuario antes de sobrescribir):

`cp {{[-i|--interactive]}} {{*.txt}} {{ruta/al/directorio_de_objetivo}}`

- Sigue los enlaces simbólicos antes de copiar:

`cp {{[-L|--dereference]}} {{enlace}} {{ruta/al/directorio_de_destino}}`

- Utiliza el primer argumento como directorio de destino (útil para `xargs ... | cp -t <DEST_DIR>`):

`cp {{[-t|--target-directory]}} {{ruta/a/directorio_de_destino}} {{ruta/a/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...}}`
