# sed

> Edita texto de manera scriptable.
> Vea también: `awk`, `ed`.
> Más información: <https://www.gnu.org/software/sed/manual/sed.html>.

- Reemplaza todas las ocurrencias de `apple` (regex básica) por `mango` (regex básica) en todas las líneas de entrada y muestra el resultado en `stdout`:

`{{comando}} | sed 's/apple/mango/g'`

- Reemplaza todas las ocurrencias de `apple` (regex extendida) por `APPLE` (regex extendida) en todas las líneas de entrada y muestra el resultado en `stdout`:

`{{comando}} | sed -E 's/(apple)/\U\1/g'`

- Reemplaza todas las ocurrencias de `apple` (regex básica) por `mango` (regex básica) en un archivo específico y sobrescribe el archivo original en su lugar:

`sed -i 's/apple/mango/g' {{ruta/al/archivo}}`

- Ejecuta un archivo de script específico y muestra el resultado en `stdout`:

`{{comando}} | sed -f {{ruta/al/script.sed}}`

- Imprime solo la primera línea en `stdout`:

`{{comando}} | sed -n '1p'`

- Elimina la primera línea de un archivo:

`sed -i 1d {{ruta/al/archivo}}`

- [I]nserta una nueva línea en la primera línea de un archivo:

`sed -i '1i\tu texto de nueva línea\' {{ruta/al/archivo}}`
