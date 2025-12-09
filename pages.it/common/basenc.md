# basenc

> Codifica o decodifica un file o `stdin` usando una codifica specificata, inviando il risultato a `stdout`.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/basenc-invocation.html>.

- Codifica un file con codifica base64:

`basenc --base64 {{percorso/del/file}}`

- Decodifica un file con codifica base64:

`basenc {{[-d|--decode]}} --base64 {{percorso/del/file}}`

- Codifica da `stdin` con codifica base32 e 42 colonne:

`{{comando}} | basenc --base32 {{[-w|--wrap]}} 42`

- Codifica da `stdin` con codifica base32:

`{{comando}} | basenc --base32`
