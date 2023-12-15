# lpoptions

> Exibir ou definir opções e padrões de uma impressora.
> Veja também: `lpadmin`.
> Mais informações: <https://www.cups.org/doc/man-lpoptions.html>.

- Definir a impressora padrão:

`lpoptions -d {{impressora[/instância]}}`

- Listar opções específicas de uma impressora:

`lpoptions -d {{impressora}} -l`

- Definir uma nova opção em uma impressora:

`lpoptions -d {{impressora}} -o {{opção[=valor]}}`

- Excluir as opções de uma impressora específica:

`lpoptions -d {{impressora}} -x`
