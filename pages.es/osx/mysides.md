# mysides

> Añade, lista y elimina favoritos del Finder.
> Más información: <https://github.com/mosen/mysides>.

- Lista favoritos de la barra lateral:

`mysides list`

- Añade un nuevo elemento al final de los favoritos de la barra lateral:

`mysides add {{ejemplo}} {{file:///Usuarios/Compartidos/ejemplo}}`

- Elimina un elemento por su nombre:

`mysides remove {{ejemplo}}`

- Añade el directorio actual a la barra lateral:

`mysides add $(basename $(pwd)) file:///$(pwd)`

- Elimina el directorio actual de la barra lateral:

`mysides remove $(basename $(pwd))`
