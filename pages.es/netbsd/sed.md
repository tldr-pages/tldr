# sed

> Edita texto de manera programable.
> Vea también: `awk`, `ed`.
> Más información: <https://man.netbsd.org/sed.1>.

- Reemplaza todas las ocurrencias de `apple` (`regex` básica) por `mango` (`regex` básica) en todas las líneas de entrada e imprime el resultado en `stdout`:

`{{comando}} | sed 's/apple/mango/g'`

- Ejecuta un [f]ichero con un script e imprime el resultado en `stdout`:

`{{comando}} | sed -f {{ruta/al/script.sed}}`

- Retrasa abrir cada archivo hasta que se aplique a una línea de entrada un comando que contenga la función `w` u otra similar:

`{{comando}} | sed -fa {{ruta/al/script.sed}}`

- Activa la extensión de [g]NU de `regex`:

`{{comando}} | sed -fg {{ruta/al/script.sed}}`

- Sustituye todas las ocurrencias de `apple` (`regex` extendida) por `APPLE` (`regex` extendida) en todas las líneas de entrada e imprime el resultado en `stdout`:

`{{comando}} | sed -E 's/(apple)/\U\1/g'`

- Imprime solo la primera línea en `stdout`:

`{{comando}} | sed -n '1p'`

- Sustituye todas las apariciones de `apple` (`regex` básica) por `mango` (`regex` básica) en un archivo específico y sobrescribe el archivo original en su lugar:

`sed -i 's/apple/mango/g' {{ruta/al/archivo}}`
