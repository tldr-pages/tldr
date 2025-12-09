# lprm

> Cancela trabalhos de impressão na fila de um servidor.
> Veja também: `lpq`.
> Mais informações: <https://openprinting.github.io/cups/doc/man-lprm.html>.

- Cancela o trabalho atual na impressora padrão:

`lprm`

- Cancela um trabalho de um servidor específico:

`lprm -h {{servidor[:porta]}} {{id_do_trabalho}}`

- Cancela múltiplos trabalhos com uma conexão criptografada com o servidor:

`lprm -E {{id_do_trabalho1 id_do_trabalho2 ...}}`

- Cancela todos os trabalhos:

`lprm -`

- Cancela o trabalho atual de uma impressora ou classe específica:

`lprm -P {{destino[/instância]}}`
