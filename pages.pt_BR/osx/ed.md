# ed

> Editor de texto original do Unix.
> Veja também: `awk`, `sed`.
> Mais informações: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Inicia uma sessão interativa do editor com um documento vazio:

`ed`

- Inicia uma sessão interativa do editor com um documento vazio e um [p]rompt específico:

`ed -p '> '`

- Inicia uma sessão interativa do editor com um documento vazio e sem diagnósticos, contagens de bytes, e prompt '!':

`ed -s`

- Edita um arquivo específico (mostra a contagem de bytes do arquivo carregado):

`ed {{caminho/para/arquivo}}`

- Substitui uma string por uma substituição específica em todas as linhas:

`,s/{{expressão_regular}}/{{substituição}}/g`
