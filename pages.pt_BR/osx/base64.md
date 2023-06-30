# base64

> Codifica e decodifica usando a representação Base64.
> Mais informações: <https://www.unix.com/man-page/osx/1/base64/>.

- Codificar um arquivo:

`base64 --input={{arquivo}}`

- Decodificar um arquivo:

`base64 --decode --input={{arquivo_base64}}`

- Codificar de `stdin`:

`echo -n "{{texto}}" | base64`

- Decodificar de `stdin`:

`echo -n {{texto_base64}} | base64 --decode`
