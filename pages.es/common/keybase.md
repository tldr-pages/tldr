# keybase

> Directorio clave que asigna identidades de redes sociales a claves de cifrado de forma públicamente auditable.
> Más información: <https://book.keybase.io/docs/cli>.

- Sigue a otro usuario:

`keybase follow {{usuario}}`

- Añade una nueva prueba:

`keybase prove {{servicio}} {{usuario_en_el_servicio}}`

- Firma un archivo:

`keybase sign {{[-i|--infile]}} {{archivo_de_entrada}} {{[-o|--outfile]}} {{archivo_de_salida}}`

- Verifica un archivo firmado:

`keybase verify {{[-i|--infile]}} {{archivo_de_entrada}} {{[-o|--outfile]}} {{archivo_de_salida}}`

- Encripta un archivo:

`keybase encrypt {{[-i|--infile]}} {{archivo_de_entrada}} {{[-o|--outfile]}} {{archivo_de_salida}} {{receptor}}`

- Desencripta un archivo:

`keybase decrypt {{[-i|--infile]}} {{archivo_de_entrada}} {{[-o|--outfile]}} {{archivo_de_salida}}`

- Revoca el dispositivo actual, cierra la sesión y elimina los datos locales:

`keybase deprovision`
