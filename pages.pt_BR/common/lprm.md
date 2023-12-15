# lprm

> Cancela trabalhos de impressão na fila de um servidor.
> Veja também: `lpq`.
> Mais informações: <https://www.cups.org/doc/man-lprm.html>.

- Cancelar o trabalho atual na impressora padrão:

`lprm`

- Cancelar um trabalho de um servidor específico:

`lprm -h {{servidor[:porta]}} {{id_do_trabalho}}`

- Cancelar múltiplos trabalhos com uma conexão criprografada com o servidor:

`lprm -E {{id_do_trabalho1 id_do_trabalho2 ...}}`

- Cancelar todos os trabalhos:

`lprm -`

- Cancelar o trabalho atual de uma impressora ou classe específica:

`lprm -P {{destino[/instância]}}`
