# lpoptions

> Exibe ou define opções e padrões de uma impressora.
> Veja também: `lpadmin`.
> Mais informações: <https://www.cups.org/doc/man-lpoptions.html>.

- Define a impressora padrão:

`lpoptions -d {{impressora[/instância]}}`

- Lista opções específicas de uma impressora:

`lpoptions -d {{impressora}} -l`

- Define uma nova opção em uma impressora:

`lpoptions -d {{impressora}} -o {{opção[=valor]}}`

- Exclui as opções de uma impressora específica:

`lpoptions -d {{impressora}} -x`
