# docker container cp

> Copia archivos o directorios entre los sistemas de archivos del host y del contenedor.
> Más información: <https://docs.docker.com/reference/cli/docker/container/cp/>.

- Copia un archivo o directorio del host a un contenedor:

`docker {{[cp|container cp]}} {{ruta/al/archivo_o_directorio_en_el_host}} {{nombre_del_contenedor}}:{{ruta/al/archivo_o_directorio_en_el_contenedor}}`

- Copia un archivo o directorio de un contenedor al host:

`docker {{[cp|container cp]}} {{nombre_del_contenedor}}:{{ruta/al/archivo_o_directorio_en_el_contenedor}} {{ruta/al/archivo_o_directorio_en_el_host}}`

- Copia un archivo o directorio desde el host a un contenedor, siguiendo los enlaces simbólicos (copia directamente los archivos enlazados, no los enlaces simbólicos en sí):

`docker {{[cp|container cp]}} {{[-L|--follow-link]}} {{path/to/symlink_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`
