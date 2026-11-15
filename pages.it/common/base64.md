# base64

> Codifica o decodifica file o `stdin` in Base64 su `stdout`.
> Maggiori informazioni: <https://manned.org/base64>.

- Codifica un file:

`base64 {{percorso/del/file}}`

- Avvolgi l'output codificato a una larghezza specifica (`0` disabilita l'avvolgimento):

`base64 {{[-w|--wrap]}} {{0|76|...}} {{percorso/del/file}}`

- Decodifica un file:

`base64 {{[-d|--decode]}} {{percorso/del/file}}`

- Codifica da `stdin`:

`{{comando}} | base64`

- Decodifica da `stdin`:

`{{comando}} | base64 {{[-d|--decode]}}`
