# cupsd

> Daemon de servidor para o servidor de impressão CUPS.
> Mais informações: <https://openprinting.github.io/cups/doc/man-cupsd.html>.

- Inicia o `cupsd` em segundo plano, ou seja, como um daemon:

`cupsd`

- Inicia o `cupsd` em primeiro plano:

`cupsd -f`

- Inicia o `cupsd` sob demanda (usado comumente pelo `launchd` ou `systemd`):

`cupsd -l`

- Inicia o `cupsd` usando o arquivo de configuração [`c`]`upsd.conf`:

`cupsd -c {{caminho/para/cupsd.conf}}`

- Inicia o `cupsd` usando os arquivos de configuração no arquivo `cups-file`[`s`]`.conf`:

`cupsd -s {{caminho/para/arquivos-cups.conf}}`

- [t]esta o arquivo de configuração [`c`]`upsd.conf` por erros:

`cupsd -t -c {{caminho/para/cupsd.conf}}`

- [t]esta os arquivos de configuração no arquivo `cups-file`[`s`]`.conf` por erros:

`cupsd -t -s {{caminho/para/arquivos-cups.conf}}`

- Mostra todas as opções disponíveis:

`cupsd -h`
