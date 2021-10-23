# date

> Define ou exibe a data e horário do sistema.
> Mais informações: <https://www.gnu.org/software/coreutils/date>.

- Exibe a data atual usando a formatação padrão:

`date +"%c"`

- Exibe a data atual no formato UTC e ISO 8601:

`date -u +"%Y-%m-%dT%H:%M:%SZ"`

- Mostra a data atual em Unix timestamp - segundos desde 00:00:00 UTC de 1 de janeiro de 1970 (Unix epoch):

`date +%s`

- Exibe uma data representada como Unix timestamp utilizando a formatação padrão:

`date -d @1473305798`

- Converte uma data específica pra Unix timestamp:

`date -d "{{2018-09-01 00:00}}" +%s --utc`

- Exibe a data atual no formato RFC-3339 (`YYYY-MM-DD hh:mm:ss TZ`):

`date --rfc-3339=s`
