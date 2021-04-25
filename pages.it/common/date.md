# date

> Imposta o mostra data e ora di sistema.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/date>.

- Mostra la data corrente utilizzando il formato predefinito della locale corrente:

`date +"%c"`

- Mostra la data corrente in UTC e formato ISO 8601:

`date -u +"%Y-%m-%dT%H:%M:%S%Z"`

- Mostra la data corrente come timestamp Unix (secondi dall'epoca Unix):

`date +%s`

- Mostra una specifica data (rappresentata come timestamp Unix) utilizzando il formato predefinito:

`date -d @1473305798`

- Converti una specifica data in un timestamp Unix:

`date -d "{{2018-09-01 00:00}}" +%s --utc`
