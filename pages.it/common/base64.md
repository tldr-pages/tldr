# base64

> Codifica o decodifica file o standard input in Base64 su standard output.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/base64>.

- Codifica un file:

`base64 {{nome_file}}`

- Decodifica un file:

`base64 --decode {{nome_file}}`

- Codifica da `stdin`:

`{{comando}} | base64`

- Decodifica da `stdin`:

`{{comando}} | base64 --decode`
