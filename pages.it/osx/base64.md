# base64

> Codifica e decodifica utilizzando la rappresentazione in base64.
> Maggiori informazioni: <https://www.unix.com/man-page/osx/1/base64/>.

- Codifica un file:

`base64 -i {{file_da_codificare}}`

- Decodifica un file:

`base64 --decode -i {{file_da_decodificare}}`

- Codifica da `stdin`:

`echo -n {{testo_da_codificare}} | base64`

- Decodifica da `stdin`:

`echo -n {{testo_da_decodificare}} | base64 --decode`
