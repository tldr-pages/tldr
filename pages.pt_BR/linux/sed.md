# sed

> Edita texto de uma maneira programável.
> Veja também: `awk`, `ed`.
> Mais informações: <https://www.gnu.org/software/sed/manual/sed.html>.

- Substitui todas as ocorrências de `apple` (regex básica) por `mango` (regex básica) em todas as linhas de entrada e imprime o resultado na `stdout`:

`{{comando}} | sed 's/apple/mango/g'`

- Executa um arquivo de script específico e imprime o resultado na `stdout`:

`{{comando}} | sed -f {{caminho/para/script.sed}}`

- Substitui todas as ocorrências de `apple` (regex estendida) por `APPLE` (regex estendida) em todas as linhas de entrada e imprime o resultado na `stdout`:

`{{comando}} | sed -E 's/(apple)/\U\1/g'`

- Imprime apenas uma primeira linha na `stdout`:

`{{comando}} | sed -n '1p'`

- Substitui todas as ocorrências de `apple` (regex básica) por `mango` (regex básica) em um arquivo específico e sobrescreve o arquivo original no lugar:

`sed -i 's/apple/mango/g' {{caminho/para/arquivo}}`
