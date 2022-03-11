# tree

> Muestra los contenidos del directorio actual en forma de árbol.
> Más información: <http://mama.indstate.edu/users/ice/tree/>.

- Imprime archivos y directories hasta `num` niveles de profundidad (donde 1 significa el directorio actual):

`tree -L {{num}}`

- Imprime solo directorios:

`tree -d`

- Imprime también archivos ocultos, coloreando la salida:

`tree -a -C`

- Imprime el árbol sin sangría, mostrando la ruta completa en su lugar (use `-N` para evitar escapar caracteres no imprimibles):

`tree -i -f`

- Imprime el tamaño de cada archivo y el tamaño total de cada directorio en formato legible para humanos:

`tree -s -h --du`

- Imprime archivos dentro de la jerarquía de árbol, especificando un patrón comodín, excluyendo los directorios que no contengan archivos coincidentes:

`tree -P '{{*.txt}}' --prune`

- Imprime archivos dentro de la jerarquía de árbol, especificando un patrón, excluyendo los directorios que no sean ancestros del especificado:

`tree -P {{nombre_del_directorio}} --matchdirs --prune`

- Imprime el árbol ignorando los directorios especificados:

`tree -I '{{nombre_del_directorio1|nombre_del_directorio2}}'`
