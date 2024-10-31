# cal

> Mostra um calendário com o dia atual destacado.
> Mais informações: <https://man.freebsd.org/cgi/man.cgi?cal>.

- Exibe um calendário para o mês atual:

`cal`

- Exibe um calendário para um ano específico:

`cal {{ano}}`

- Exibe um calendário para um ano e mês específicos:

`cal {{mês}} {{ano}}`

- Exibe o calendário inteiro para o ano atual:

`cal -y`

- Não destaca hoje e exibe [3] meses abrangendo a data:

`cal -h -3 {{mês}} {{ano}}`

- Exibe os 2 meses [A]ntes e 3 [D]epois de um [m]ês específico do ano atual:

`cal -A 3 -B 2 {{mês}}`

- Exibe dias [j]ulianos (começando de um, numerados de 1º de janeiro):

`cal -j`
