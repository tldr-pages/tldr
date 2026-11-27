# ac

> Imprime estatísticas de quanto tempo usuários permaneceram conctados.
> Mais informações: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Imprime quanto tempo em horas o usuário atual ficou conectado:

`ac`

- Imprime quanto tempo em horas usuários ficaram conectados:

`ac {{[-p|--individual-totals]}}`

- Imprime quanto tempo em horas um usuário em particular ficou conectado:

`ac {{[-p|--individual-totals]}} {{nome_do_usuario}}`

- Imprime quanto tempo um usuário em particular ficou conectado em horas por dia (com total):

`ac {{[-d|--daily-totals]}} {{[-p|--individual-totals]}} {{nome_do_usuario}}`

- Também exibe detalhes adicionais:

`ac --compatibility`
