# export

> Exporta variables de un intérprete de comandos (shell) a procesos hijos.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- Establece una variable de entorno:

`export {{VARIABLE}}={{valor}}`

- Quita una variable de entorno:

`export -n {{VARIABLE}}`

- Exporta una función a los procesos hijos:

`export -f {{NOMBRE_FUNCION}}`

- Añade una ruta a la variable de ambiente `PATH`:

`export PATH=$PATH:{{ruta/a/añadir}}`

- Muestra una lista de variables exportadas activas en forma de comando de interfaz de comandos (shell command form):

`export -p`
