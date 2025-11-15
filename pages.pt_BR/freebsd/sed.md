# sed

> Edita texto de uma maneira programável.
> Veja também: `awk`, `ed`.
> Mais informações: <https://www.freebsd.org/cgi/man.cgi?sed>.

- Substitui todas as ocorrências de `maçã` (regex básico) por `manga` (regex básico) em todas as linhas de entrada e imprime o resultado para `stdout`:

`{{comando}} | sed 's/maçã/manga/g'`

- Executa um script específico e imprime o resultado para `stdout`:

`{{comando}} | sed -f {{caminho/para/script.sed}}`

- Atrasa a abertura de cada arquivo até que um comando contendo a função ou flag `w` relacionada seja aplicada a linha de entrada:

`{{comando}} | sed -fa {{caminho/para/script.sed}}`

- Substitui todas as ocorrências de `maçã` (regex extendido) por `MAÇÃ` (regex extendido) em todas as linhas de entrada e imprime o resultado para `stdout`:

`{{comando}} | sed -E 's/(maçã)/\U\1/g'`

- Imprime apenas a primeira linha para `stdout`:

`{{comando}} | sed -n '1p'`

- Substitui todas as ocorrências de `maçã` (regex básico) por `manga` (regex básico) em um arquivo específico e sobrescreve o arquivo original no lugar:

`sed -i 's/maçã/manga/g' {{caminho/para/arquivo}}`
