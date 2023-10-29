# sed

> Edita texto de manera programable.
> Ver también: `awk`, `ed`.
> Más información: <https://keith.github.io/xcode-man-pages/sed.1.html>.

- Reemplaza todas las veces que aparece `apple` (regex básico) por `mango` (regex básico) en todas las líneas de entrada e imprime el resultado en `stdout`:

`{{command}} | sed 's/apple/mango/g'`

- Ejecuta un script [f] específico e imprime el resultado en `stdout`:

`{{command}} | sed -f {{ruta/al/archivo_script.sed}}`

- Sustituye todas las apariciones de `manzana` (regex extendido) por `MANZANA` (regex extendido) en todas las líneas de entrada e imprime el resultado en `stdout`:

`{{command}} | sed -E 's/(manzana)/\U\1/g'`

- Imprime solo la primera línea en `stdout`:

`{{command}} | sed -n '1p'`

- Sustituye todas las apariciones de `manzana` (regex básico) por `mango` (regex básico) en un `fichero` y guarda una copia de seguridad del original en `fichero.bak`:

`sed -i bak 's/manzana/mango/g' {{ruta/al/archivo}}`
