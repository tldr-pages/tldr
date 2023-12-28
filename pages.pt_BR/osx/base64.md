# base64

> Codifica e decodifica usando a representação Base64.
> Mais informações: <https://www.unix.com/man-page/osx/1/base64/>.

- Codifica um arquivo:

`base64 --input={{arquivo}}`

- Decodifica um arquivo:

`base64 --decode --input={{arquivo_base64}}`

- Codifica de `stdin`:

`echo -n "{{texto}}" | base64`

- Decodifica de `stdin`:

`echo -n {{texto_base64}} | base64 --decode`
