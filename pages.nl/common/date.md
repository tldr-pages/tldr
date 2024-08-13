# date

> Stel de systeemdatum in of toon deze.
> Meer informatie: <https://www.gnu.org/software/coreutils/date>.

- Toon de huidige datum in het standaardformaat van de locale:

`date +%c`

- Toon de huidige datum in UTC, in het ISO 8601-formaat:

`date -u +%Y-%m-%dT%H:%M:%S%Z`

- Toon de huidige datum als een Unix timestamp (seconden sinds de Unix-epoch):

`date +%s`

- Converteer een datum gespecificeerd als een Unix timestamp naar het standaard formaat:

`date -d @{{1473305798}}`

- Converteer een opgegeven datum naar het Unix timestamp formaat:

`date -d "{{2018-09-01 00:00}}" +%s --utc`

- Toon de huidige datum in het RFC-3339 formaat (`YYYY-MM-DD hh:mm:ss TZ`):

`date --rfc-3339 s`

- Stel de huidige datum in met het formaat `MMDDhhmmYYYY.ss` (`YYYY` en `.ss` zijn optioneel):

`date {{093023592021.59}}`

- Toon het huidige ISO-weeknummer:

`date +%V`
