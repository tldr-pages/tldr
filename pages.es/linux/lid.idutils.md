# lid

> Consulta una base de datos de ID en busca de tokens que coincidan con un patrón.
> Nota: Primero hay que crear una base de datos de ID utilizando `mkid`.
> Más información: <https://www.gnu.org/software/idutils/manual/idutils.html#lid-invocation>.

- Muestra todos los tokens y la ubicación de sus archivos en la base de datos de ID:

`lid`

- Busca archivos que contengan un token específico:

`lid {{token}}`

- Busca tokens que coincidan con un patrón, sin distinguir entre mayúsculas y minúsculas:

`lid {{[-i|--ignore-case]}} {{token}}`

- Busca tokens que coincidan con una `regex` ampliada:

`lid {{[-r|--regexp]}} "{{patrón}}"`

- Muestra las líneas coincidentes en formato tipo grep:

`lid {{[-R|--result]}} grep {{token}}`

- Busca tokens que aparezcan solo una vez (útil para encontrar definiciones no utilizadas):

`lid {{[-F|--frequency]}} 1`
