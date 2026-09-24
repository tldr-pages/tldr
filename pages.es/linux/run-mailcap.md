# run-mailcap

> Ejecuta programas mediante las entradas del archivo `mailcap`.
> Más información: <https://manned.org/run-mailcap>.

- Edita cualquier archivo existente o crea uno nuevo con la herramienta de edición predeterminada de `mailcap`:

`run-mailcap --action=compose {{ruta/al/archivo}}`

- Muestra cualquier archivo en el explorador predeterminado de `mailcap`:

`run-mailcap --action=edit {{ruta/al/archivo}}`

- Imprime un archivo utilizando la herramienta de impresión predeterminada de `mailcap`:

`run-mailcap --action=print {{ruta/al/archivo}}`

- Muestra cualquier archivo (normalmente una imagen) en el explorador predeterminado de `mailcap`:

`run-mailcap --action=view {{ruta/al/archivo}}`

- Ejecuta acciones o programas individuales en `run-mailcap`:

`run-mailcap --action={{view|cat|compose|composetyped|edit|print}} {{ruta/al/archivo}}`

- Activa información adicional:

`run-mailcap --action={{action}} --debug {{ruta/al/archivo}}`

- Ignora cualquier directiva «copiousoutput» y redirigir la salida a `stdout`:

`run-mailcap --action={{action}} --nopager {{ruta/al/archivo}}`

- Muestra el comando encontrado sin ejecutarlo realmente:

`run-mailcap --action={{action}} --norun {{ruta/al/archivo}}`
