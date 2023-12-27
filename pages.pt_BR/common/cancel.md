# cancel

> Cancela trabalhos de impressão.
> Veja também: `lp`, `lpmove`, `lpstat`.
> Mais informações: <https://openprinting.github.io/cups/doc/man-cancel.html>.

- Cancela o trabalho atual da impressora padrão (definida com `lpoptions -d {{impressora}}`):

`cancel`

- Cancela todos os trabalhos da impressora padrão que pertencem a um usuário específico:

`cancel -u {{nome_do_usuário}}`

- Cancela o trabalho atual de uma impressora específica:

`cancel {{impressora}}`

- Cancela um trabalho específico de uma impressora específica:

`cancel {{impressora}}-{{id_do_trabalho}}`

- Cancela todos os trabalhos de todas as impressoras:

`cancel -a`

- Cancela todos os trabalhos de uma impressora específica:

`cancel -a {{impressora}}`

- Cancela o trabalho atual de um servidor específico e então deleta os arquivos de dados do trabalho:

`cancel -h {{servidor}} -x`
