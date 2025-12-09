# comm

> Selecciona o rechaza las líneas comunes a dos ficheros. Ambos ficheros deben estar ordenados.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/comm-invocation.html>.

- Produce tres columnas separadas por tabuladores: líneas solo en el primer archivo, líneas solo en el segundo archivo y líneas comunes:

`comm {{fichero1}} {{fichero2}}`

- Imprime solo las líneas comunes a ambos archivos:

`comm -12 {{fichero1}} {{fichero2}}`

- Imprime solo las líneas comunes a ambos archivos, leyendo un archivo desde `stdin`:

`cat {{fichero1}} | comm -12 - {{fichero2}}`

- Obtiene las líneas que solo se encuentran en el primer fichero, guardando el resultado en un tercer fichero:

`comm -23 {{fichero1}} {{fichero2}} > {{solo_fichero1}}`

- Imprime las líneas solo encontradas en el segundo fichero, cuando los ficheros no están ordenados:

`comm -13 <( sort {{fichero1}}) <( sort {{fichero2}})`
