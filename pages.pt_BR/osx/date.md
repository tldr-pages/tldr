# date

> Define ou exibe a data do sistema.
> Mais informações: <https://keith.github.io/xcode-man-pages/date.1.html>.

- Exibe a data atual usando o formato da localidade padrão:

`date +%c`

- Exibe a data atual no formato UTC e ISO 8601:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- Exibe a data atual como um timestamp Unix (segundos desde a época Unix):

`date +%s`

- Exibe uma data específica (representada como um timestamp Unix) usando o formato padrão:

`date -r 1473305798`
