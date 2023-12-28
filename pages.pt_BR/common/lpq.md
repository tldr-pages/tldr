# lpq

> Mostra o estado da fila de impressão.
> Mais informações: <https://openprinting.github.io/cups/doc/man-lpq.html>.

- Mostra os trabalhos na fila do destino padrão:

`lpq`

- Mostra os trabalhos na fila de todas as impressoras usando criptografia:

`lpq -a -E`

- Mostra os trabalhos da fila em um formato longo:

`lpq -l`

- Mostra os trabalhos da fila de uma impressora ou classe específica:

`lpq -P {{destino[/instância]}}`

- Mostra os trabalhos na fila a cada n segundos até que a fila esteja vazia:

`lpq +{{intervalo}}`
