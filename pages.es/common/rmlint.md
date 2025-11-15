# rmlint

> Encuentra desperdicio de espacio y otras cosas rotas en tu sistema de archivos.
> Más información: <https://rmlint.readthedocs.io/en/latest/rmlint.1.html>.

- Comprueba los directorios en busca de archivos duplicados, vacíos y rotos:

`rmlint {{ruta/a/directorio1 ruta/a/directorio2 ...}}`

- Comprueba si hay duplicados mayores a un tamaño determinado, preferiblemente manteniendo los archivos en directorios etiquetados (después de la doble barra):

`rmlint -s {{1MB}} {{ruta/a/directorio}} // {{ruta/a/directorio_original}}`

- Comprueba que no se desperdicia espacio, manteniendo todo en los directorios no etiquetados:

`rmlint --keep-all-untagged {{ruta/a/directorio}} // {{ruta/a/directorio_original}}`

- Elimina archivos duplicados encontrados tras una ejecución de `rmlint`:

`./rmlint.sh`

- Encuentra árboles de directorios duplicados basándose en los datos, ignorando los nombres:

`rmlint --merge-directories {{ruta/a/directorio}}`

- Marca archivos en la profundida[d] de la ruta inferior como originales, en caso de igualdad elegir uno más corto [l]:

`rmlint --rank-by={{dl}} {{ruta/a/directorio}}`

- Encuentra archivos con idéntico nombre de archivo y contenido, y vincula en lugar de eliminar los duplicados:

`rmlint -c sh:link --match-basename {{ruta/a/directorio}}`

- Utiliza `data` como directorio maestro. Busca solo los duplicados de la copia de seguridad que también estén en `datos`. No elimina ningún archivo de "datos":

`rmlint {{ruta/a/copia}} // {{ruta/a/datos}} --keep-all-tagged --must-match-tagged`
