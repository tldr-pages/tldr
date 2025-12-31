# base64

> Codifica e decodifica usando a representação Base64.
> Mais informações: <https://keith.github.io/xcode-man-pages/bintrans.1>.

- Codifica um arquivo:

`base64 {{[-i|--input]}} {{arquivo}}`

- Decodifica um arquivo:

`base64 {{[-d|--decode]}} {{[-i|--input]}} {{arquivo_base64}}`

- Codifica de `stdin`:

`echo -n "{{texto}}" | base64`

- Decodifica de `stdin`:

`echo -n {{texto_base64}} | base64 {{[-d|--decode]}}`
