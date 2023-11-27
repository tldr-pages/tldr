# calc

> Uma calculadora interativa de precisão arbitrária no terminal.
> Mais informações: <https://github.com/lcn2/calc>.

- Inicia a `calc` no modo interativo:

`calc`

- Realiza um cálculo no modo não interativo:

`calc '{{85 * (36 / 4)}}'`

- Realiza um cálculo sem qualquer formatação de saída (para usar com pipes):

`calc -p '{{4/3 * pi() * 5^3}}'`

- Realiza um cálculo e, em seguida, altera para o modo [i]nterativo:

`calc -i '{{sqrt(2)}}'`

- Inicia `calc` em um [m]odo de permissão específico (0 até 7, o padrão é 7):

`calc -m {{modo}}`

- Exibe uma introdução à `calc`:

`calc help intro`

- Exibe uma visão geral da `calc`:

`calc help overview`

- Abre o manual da `calc`:

`calc help`
