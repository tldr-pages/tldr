# sed

> Edita texto de manera scriptable.
> Vea también: `awk`, `ed`.
> Más información: <https://manned.org/sed.1posix>.

- Reemplaza todas las ocurrencias de `apple` (regex básica) por `mango` (regex básica) en todas las líneas de entrada y muestra el resultado en `stdout`:

`{{comando}} | sed 's/apple/mango/g'`

- Ejecuta un archivo de script específico y muestra el resultado en `stdout`:

`{{comando}} | sed -f {{ruta/al/script.sed}}`

- Imprime solo la primera línea en `stdout`:

`{{comando}} | sed -n '1p'`
