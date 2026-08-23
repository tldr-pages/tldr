# zoxide

> Realiza un seguimiento de los directorios más utilizados.
> Utiliza un algoritmo de clasificación para navegar a la mejor coincidencia.
> Más información: <https://manned.org/zoxide>.

- Va al directorio mejor clasificado que contiene una `cadena` en su nombre:

`zoxide query string`

- Va al directorio mejor clasificado que contiene `string1` y luego `string2`:

`zoxide query string1 string2`

- Inicia una búsqueda interactiva de directorios (requiere `fzf`):

`zoxide query {{[-i|--interactive]}}`

- Añade un directorio o incrementa su rango:

`zoxide add {{ruta/al/directorio}}`

- Elimina un directorio de la base de datos de `zoxide`:

`zoxide remove {{ruta/al/directorio}}`

- Genera la configuración de la terminal para los alias de comandos (`z`, `zi`):

`zoxide init {{bash|elvish|fish|nushell|posix|powershell|tcsh|xonsh|zsh}}`
