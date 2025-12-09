# base32

> Codifica o decodifica file o standard input in Base32 su standard output.
> Maggiori informazioni: <https://manned.org/base32>.

- Codifica un file:

`base32 {{percoso/del/file}}`

- Avvolgi l'output codificato a una larghezza specifica (`0` disabilita l'avvolgimento):

`base32 {{[-w|--wrap]}} {{0|76|...}} {{percoso/del/file}}`

- Decodifica un file:

`base32 {{[-d|--decode]}} {{percoso/del/file}}`

- Codifica da `stdin`:

`{{comando}} | base32`

- Decodifica da `stdin`:

`{{comando}} | base32 {{[-d|--decode]}}`
