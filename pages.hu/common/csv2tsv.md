# csv2tsv

> A CSV (vesszővel elválasztott) szöveget TSV (tabulátorral elválasztott) formátumba konvertálja. További információ: <https://github.com/eBay/tsv-utils/blob/master/README.md#csv2tsv>.

- Konvertálás CSV formátumból TSV formátumba:

`csv2tsv {{path/to/input_csv1 path/to/input_csv2 ...}} > {{path/to/output_tsv}}`

- A mezővel elválasztott CSV mezővel elválasztott CSV-t TSV-be konvertálja:

`csv2tsv -c'{{field_delimiter}}' {{path/to/input_csv}}`

- Szvsz elválasztott CSV átalakítása TSV-be:

`csv2tsv -c';' {{path/to/input_csv}}`
