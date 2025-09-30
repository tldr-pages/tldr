# sed

> Edita texto de uma maneira programável.
> Veja também: `awk`, `ed`.
> Mais informações: <https://www.gnu.org/software/sed/manual/sed.html>.

- Substitui todas as ocorrências de `apple` (regex básica) por `mango` (regex básica) em todas as linhas de entrada e imprime o resultado na `stdout`:

`{{comando}} | sed 's/apple/mango/g'`

- Substitui todas as ocorrências de `apple` (regex estendida) por `APPLE` (regex estendida) em todas as linhas de entrada e imprime o resultado na `stdout`:

`{{comando}} | sed {{[-E|--regexp-extended]}} 's/(apple)/\U\1/g'`

- Substitui todas as ocorrências de `apple` (regex básica) por `mango` (regex básica) em um arquivo específico e sobrescreve o arquivo original:

`sed {{[-i|--in-place]}} 's/apple/mango/g' {{caminho/para/arquivo}}`

- Executa um arquivo de script específico e imprime o resultado na `stdout`:

`{{comando}} | sed {{-f|--file}} {{caminho/para/script.sed}}`

- Imprime apenas uma primeira linha na `stdout`:

`{{comando}} | sed {{[-n|--quiet]}} '1p'`

- Exclui a primeira linha de um arquivo:

`sed {{[-i|--in-place]}} 1d {{caminho/para/arquivo}}`

- Adiciona uma nova linha na primeira linha de um arquivo:

`sed {{[-i|--in-place]}} '1i\sua nova linha de texto\' {{caminho/para/arquivo}}`
