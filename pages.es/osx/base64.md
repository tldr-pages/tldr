# base64

> Codifica y decodifica usando la representación Base64.
> Más información: <https://keith.github.io/xcode-man-pages/base64.1.html>.

- Codifica un archivo:

`base64 --input={{archivo_plano}}`

- Decodifica un archivo:

`base64 --decode --input={{base64_archivo}}`

- Codifica desde `stdin`:

`echo -n "{{texto_plano}}" | base64`

- Decodifica desde `stdin`:

`echo -n {{base64_texto}} | base64 --decode`
