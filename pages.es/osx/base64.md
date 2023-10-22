# base64

> Codifica y decodifica usando la repesentación Base64.
> Más información: <https://www.unix.com/man-page/osx/1/base64/>.

- Codifica un archivo:

`base64 --input={{archivo_plano}}`

- Decodifica un archivo:

`base64 --decode --input={{base64_archivo}}`

- Codifica desde `stdin`:

`echo -n "{{texto_plano}}" | base64`

- Decodifica desde `stdin`:

`echo -n {{base64_texto}} | base64 --decode`
