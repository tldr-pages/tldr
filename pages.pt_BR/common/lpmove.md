# lpmove

> Move um ou todos os trabalhos para outra impressora.
> Veja também: `cancel`, `lp`, `lpr`, `lprm`.
> Mais informações: <https://openprinting.github.io/cups/doc/man-lpmove.html>.

- Move um trabalho específico para `nova_impressora`:

`lpmove {{id_do_trabalho}} {{nova_impressora}}`

- Move um trabalho de `antiga_impressora` para `nova_impressora`:

`lpmove {{antiga_impressora}}-{{id_do_trabalho}} {{nova_impressora}}`

- Move todos os trabalhos de `antiga_impressora` para `nova_impressora`:

`lpmove {{antiga_impressora}} {{nova_impressora}}`

- Move um trabalho específico para `nova_impressora` em um servidor específico:

`lpmove -h {{server}} {{id_do_trabalho}} {{nova_impressora}}`
