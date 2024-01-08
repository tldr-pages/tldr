# xattr

> Utilidad para trabajar con atributos extendidos del sistema de ficheros.
> Más información: <https://ss64.com/osx/xattr.html>.

- Lista atributos extendidos clave:valor para un archivo dado:

`xattr -l {{archivo}}`

- Escribe un atributo para un archivo determinado:

`xattr -w {{atributo_clave}} {{atributo_valor}} {{archivo}}`

- Elimina un atributo de un archivo determinado:

`xattr -d {{com.apple.quarantine}} {{archivo}}`

- Elimina todos los atributos extendidos de un archivo determinado:

`xattr -c {{archivo}}`

- Elimina recursivamente un atributo en un directorio determinado:

`xattr -rd {{clave_atributo}} {{directorio}}`
