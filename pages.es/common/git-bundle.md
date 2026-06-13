# git bundle

> Empaqueta objetos y referencias en un archivo.
> Más información: <https://git-scm.com/docs/git-bundle>.

- Crea un archivo bundle que contiene todos los objetos y referencias de una rama específica:

`git bundle create {{ruta/al/archivo.bundle}} {{nombre_rama}}`

- Crea un archivo bundle de todas las ramas:

`git bundle create {{ruta/al/archivo.bundle}} --all`

- Crea un archivo bundle de los últimos 5 commits de la rama actual:

`git bundle create {{ruta/al/archivo.bundle}} -5 {{HEAD}}`

- Crea un archivo bundle de los últimos 7 días:

`git bundle create {{ruta/al/archivo.bundle}} --since 7.days {{HEAD}}`

- Verifica que un archivo bundle es válido y puede aplicarse al repositorio actual:

`git bundle verify {{ruta/al/archivo.bundle}}`

- Imprime en `stdout` la lista de referencias contenidas en un bundle:

`git bundle unbundle {{ruta/al/archivo.bundle}}`

- Desagrupa una rama específica de un archivo bundle en el repositorio actual:

`git pull {{ruta/al/archivo.bundle}} {{nombre_rama}}`

- Crea un nuevo repositorio a partir de un paquete:

`git clone {{ruta/al/archivo.bundle}}`
