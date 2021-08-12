# date

> Setați sau afișați data sistemului.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/date>

- Afișează data curentă utilizând formatul setărilor regionale implicite:

`date +"%c"`

- Afișează data curentă în format UTC și ISO 8601:

`date -u +"%Y-%m-%dT%H:%M:%SZ"`

- Afișează data curentă ca marcă de timp Unix (secunde de la epoca Unix):

`date +%s`

- Afișează o anumită dată (reprezentată ca marcă de timp Unix) utilizând formatul implicit:

`date -d @1473305798`

- Conversia unei anumite date în formatul marcajului temporal Unix:

`date -d "{{2018-09-01 00:00}}" +%s --utc`

- Afișează data curentă utilizând formatul RFC-3339 (`AAAA-LL-ZZ hhh:mm:ss TZ`):

`date --rfc-3339=s`
