# base64

> Codifica o decodifica file o standard input in Base64 su standard output.
> Maggiori informazioni: <https://manned.org/base64>.

- Codifica un file:

`base64 {{percoso/del/file}}`

- Avvolgi l'output codificato a una larghezza specifica (`0` disabilita l'avvolgimento):

`base64 {{[-w|--wrap]}} {{0|76|...}} {{percoso/del/file}}`

- Decodifica un file:

`base64 {{[-d|--decode]}} {{percoso/del/file}}`

- Codifica da `stdin`:

`{{comando}} | base64`

- Decodifica da `stdin`:

`{{comando}} | base64 {{[-d|--decode]}}`
