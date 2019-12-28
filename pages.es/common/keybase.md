# keybase

> Directorio de claves que conecta identidades en redes sociales a claves encriptadas de una manera públicamente auditable.
> Más información: <https://keybase.io/docs/command_line>.

- Sigue a otro usuario:

`keybase follow {{nombre_de_usuario}}`

- Añade una nueva prueba:

`keybase prove {{servicio}} {{nombre_de_usuario_en_el_servicio}}`

- Firma un archivo:

`keybase sign --infile {{archivo_de_entrada}} --outfile {{archivo_de_salida}}`

- Verifica un archivo firmado:

`keybase verify --infile {{archivo_de_entrada}} --outfile {{archivo_de_salida}}`

- Encripta un archivo:

`keybase encrypt --infile {{archivo_de_entrada}} --outfile {{archivo_de_salida}} {{receptor}}`

- Desencripta un archivo:

`keybase decrypt --infile {{archivo_de_entrada}} --outfile {{archivo_de_salida}}`

- Revoca el dispositivo actual, se desconecta y borra los datos locales:

`keybase deprovision`
