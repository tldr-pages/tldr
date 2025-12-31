# csplit

> Splits een bestand in stukken.
> Dit genereert bestanden zoals `xx00`, `xx01` etc.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/csplit-invocation.html>.

- Splits een bestand in twee delen, waarbij het tweede deel begint op regel 10:

`csplit {{pad/naar/bestand}} 10`

- Splits een bestand in drie delen, waarbij de laatste delen beginnen op regel 7 en 23:

`csplit {{pad/naar/bestand}} 7 23`

- Start een nieuw deel op elke 5e regel (faalt als het aantal regels niet deelbaar is door 5):

`csplit {{pad/naar/bestand}} 5 {*}`

- Start een nieuw deel op elke 5e regel, waarbij de fout bij niet-exacte delingen wordt genegeerd:

`csplit {{[-k|--keep-files]}} {{pad/naar/bestand}} 5 {*}`

- Splits een bestand boven regel 5 en gebruik een aangepaste prefix voor de uitvoerbestanden (standaard is `xx`):

`csplit {{pad/naar/bestand}} 5 {{[-f|--prefix]}} {{prefix}}`

- Splits een bestand boven de eerste regel die overeenkomt met de `regex`:

`csplit {{pad/naar/bestand}} /{{regex}}/`
