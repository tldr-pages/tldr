# cp

> Copia archivos y directorios.
> Más información: <https://www.gnu.org/software/coreutils/cp>.

- Copia un archivo a otro directorio:

`cp {{ruta/al/archivo_origen.ext}} {{ruta/al/archivo_destino.ext}}`

- Copia un archivo en otro directorio, conservando el nombre del archivo:

`cp {{path/to/source_file.ext}} {{path/to/target_parent_directory}}`

- Copia de forma recursiva el contenido de un directorio a otra ubicación (si el destino existe, el directorio es copiado en esa ubicación):

`cp -r {{ruta/al/directorio_origen}} {{ruta/al/directorio_destino}}`

- Copia un directorio de forma recursiva en modo verbose (muestra los archivos a medida que se copian):

`cp -vr {{path/to/source_directory}} {{path/to/target_directory}}`

- Copia archivos de texto en otra ubicación en modo interactivo (pregunta al usuario antes de sobreescribir):

`cp -i {{*.txt}} {{path/to/target_directory}}`

- Sigue los enlaces simbólicos antes de copiar:

`cp -L {{link}} {{path/to/target_directory}}`

- Usa la ruta completa de los archivos de origen, creando los directorios intermedios faltantes al copiar:

`cp --parents {{source/path/to/file}} {{path/to/target_file}}`
