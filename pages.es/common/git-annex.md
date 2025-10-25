# git annex

> Administra archivos con Git sin registrar su contenido.
> Cuando se anexa un archivo, su contenido se mueve a un almacén de clave-valor y se crea un enlace simbólico que apunta a dicho contenido.
> Más información: <https://git-annex.branchable.com/git-annex/>.

- Inicializa un repositorio con Git annex:

`git annex init`

- Añade un archivo:

`git annex add {{ruta/al/archivo_o_directorio}}`

- Muestra el estado actual de un archivo o directorio:

`git annex status {{ruta/al/archivo_o_directorio}}`

- Sincroniza un repositorio local con uno remoto:

`git annex {{remoto}}`

- Obtiene un archivo o directorio:

`git annex get {{ruta/al/archivo_o_directorio}}`

- Muestra ayuda:

`git annex help`
