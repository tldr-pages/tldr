# date

> Define ou exibe a data do sistema.
> Mais informações: <https://www.gnu.org/software/coreutils/date>.

- Exibe a data atual usando o formato padrão de localidade:

`date +%c`

- Exibe a data atual em UTC, usando o formato ISO 8601:

`date -u +%Y-%m-%dT%H:%M:%S%Z`

- Exibe a data atual em Unix timestamp - segundos desde 00:00:00 UTC de 1 de janeiro de 1970 (Unix epoch):

`date +%s`

- Converte uma data especificada como Unix timestamp para o formato padrão:

`date -d @{{1473305798}}`

- Converte uma determinada data pra Unix timestamp:

`date -d "{{2018-09-01 00:00}}" +%s --utc`

- Exibe a data atual usando o formato RFC-3339 (`YYYY-MM-DD hh:mm:ss TZ`):

`date --rfc-3339=s`

- Define a data atual usando o formato `MMDDhhmmYYYY.ss` (`YYYY` e `.ss` são opcionais):

`date {{093023592021.59}}`

- Exibe o número da semana ISO atual:

`date +%V`
