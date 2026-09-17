# xxd

> Crea una representación hexadecimal (hexdump) a partir de un archivo binario, o viceversa.
> Vea también: `hexyl`, `od`, `hexdump`.
> Más información: <https://manned.org/xxd>.

- Genera un hexdump a partir de un archivo binario y muestra el resultado:

`xxd {{archivo_de_entrada}}`

- Genera un volcado hexadecimal a partir de un archivo binario y lo guarda como un archivo de texto:

`xxd {{archivo_de_entrada}} {{archivo_de_salida}}`

- Muestra una salida más compacta, sustituyendo los ceros consecutivos (si los hay) por un asterisco:

`xxd {{[-a|-autoskip]}} {{archivo_de_entrada}}`

- Muestra la salida con 10 columnas de un octeto (byte) cada una:

`xxd {{[-c|-cols]}} {{10}} {{archivo_de_entrada}}`

- Muestra la salida solo hasta una longitud de 32 bytes:

`xxd {{[-l|-len]}} {{32}} {{archivo_de_entrada}}`

- Muestra la salida en modo plano, sin espacios entre las columnas:

`xxd {{[-p|-postscript]}} {{archivo_de_entrada}}`

- Convierte un volcado hexadecimal de texto sin formato de nuevo a binario y lo guarda como un archivo binario:

`xxd {{[-r|-revert]}} {{[-p|-postscript]}} {{archivo_de_entrada}} {{archivo_de_salida}}`
