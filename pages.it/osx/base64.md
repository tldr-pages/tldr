# base64

> Codifica e decodifica utilizzando la rappresentazione in base64.
> Maggiori informazioni: <https://keith.github.io/xcode-man-pages/bintrans.1>.

- Codifica un file:

`base64 {{[-i|--input]}} {{file_da_codificare}}`

- Decodifica un file:

`base64 {{[-d|--decode]}} {{[-i|--input]}} {{file_da_decodificare}}`

- Codifica da `stdin`:

`echo -n "{{testo_da_codificare}}" | base64`

- Decodifica da `stdin`:

`echo -n {{testo_da_decodificare}} | base64 {{[-d|--decode]}}`
