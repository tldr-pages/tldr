# ed

> O editor de texto original do Unix.
> Veja também: `awk`, `sed`.
> Mais informações: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Inicia uma sessão do editor interativo com um documento vazio:

`ed`

- Inicia uma sessão do editor interativo com um documento vazio e um prompt específico:

`ed --prompt='> '`

- Inicia uma sessão do editor interativo com erros compreensíveis para usuários:

`ed --verbose`

- Inicia uma sessão do editor interativo com um documento vazio e sem diagnósticos, contagens de bytes e prompt "!":

`ed --quiet`

- Inicia uma sessão do editor interativo sem mudança no status de saída quando o comando falha:

`ed --loose-exit-status`

- Edita um arquivo específico (mostra a contagem de bytes do arquivo carregado):

`ed {{caminho/para/arquivo}}`

- Substitui a string com um substituto específico em todas as linhas:

`,s/{{regular_expression}}/{{substituto}}/g`
