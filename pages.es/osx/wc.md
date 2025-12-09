# wc

> Cuenta líneas, palabras o bytes.
> Más información: <https://keith.github.io/xcode-man-pages/wc.1.html>.

- Cuenta líneas en un archivo:

`wc -l {{ruta/al/archivo}}`

- Cuenta palabras en el archivo:

`wc -w {{ruta/al/archivo}}`

- Cuenta caracteres (bytes) en el archivo:

`wc -c {{ruta/al/archivo}}`

- Cuenta caracteres en el archivo (teniendo en cuenta los conjuntos de caracteres multibyte):

`wc -m {{ruta/al/archivo}}`

- Usa `stdin` para contar líneas, palabras y caracteres (bytes) en ese orden:

`{{find .}} | wc`
